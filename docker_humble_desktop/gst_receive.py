#!/usr/bin/env python3
import subprocess
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

CAMERAS = [
    {"udp_port": 5000, "http_port": 8080},
    {"udp_port": 5002, "http_port": 8081},
    {"udp_port": 5004, "http_port": 8082},
    {"udp_port": 5006, "http_port": 8083},
]

# One buffer of the latest JPEG per camera, shared across all clients
latest_frames = {cam["http_port"]: None for cam in CAMERAS}
frame_events = {cam["http_port"]: threading.Event() for cam in CAMERAS}


def capture_frames(udp_port, http_port):
    """Runs GStreamer once, decodes JPEG frames, stores latest in memory."""
    # Use rtpjpegdepay -> multipartmux directly to avoid decoding and re-encoding
    # This preserves the original JPEG payloads and reduces CPU and latency
    cmd = [
        "gst-launch-1.0", "-q",
        "udpsrc", f"port={udp_port}",
        "caps=application/x-rtp,encoding-name=JPEG,payload=26",
        "!", "rtpjpegdepay",
        "!", "jpegparse",
        "!", "multipartmux", "boundary=frame",
        "!", "fdsink", "fd=1",
    ]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    boundary = b"--frame"
    buf = b""
    while True:
        chunk = proc.stdout.read(4096)
        if not chunk:
            break
        buf += chunk
        # Extract complete JPEG frames from the multipart stream
        while True:
            start = buf.find(b"\xff\xd8")
            end = buf.find(b"\xff\xd9")
            if start == -1 or end == -1 or end < start:
                break
            jpeg = buf[start:end + 2]
            buf = buf[end + 2:]
            latest_frames[http_port] = jpeg
            frame_events[http_port].set()
            frame_events[http_port].clear()


class MJPEGHandler(BaseHTTPRequestHandler):
    http_port = None

    def log_message(self, format, *args):
        pass

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "multipart/x-mixed-replace; boundary=frame")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()

        try:
            while True:
                frame_events[self.http_port].wait(timeout=1.0)
                jpeg = latest_frames[self.http_port]
                if jpeg is None:
                    continue
                header = (
                    b"--frame\r\n"
                    b"Content-Type: image/jpeg\r\n"
                    b"\r\n"
                )
                self.wfile.write(header + jpeg + b"\r\n")
                self.wfile.flush()
        except Exception:
            pass


def make_handler(http_port):
    class Handler(MJPEGHandler):
        pass
    Handler.http_port = http_port
    return Handler


def serve(udp_port, http_port):
    # Start GStreamer capture thread
    t = threading.Thread(target=capture_frames, args=(udp_port, http_port), daemon=True)
    t.start()
    # Start HTTP server
    server = HTTPServer(("0.0.0.0", http_port), make_handler(http_port))
    print(f"Camera udp:{udp_port} → http://localhost:{http_port}")
    server.serve_forever()


threads = []
for cam in CAMERAS:
    t = threading.Thread(target=serve, args=(cam["udp_port"], cam["http_port"]), daemon=True)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
