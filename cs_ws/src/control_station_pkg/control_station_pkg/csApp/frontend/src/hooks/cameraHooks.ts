import React from "react";
import { useState, useEffect } from "react";
import { Cameras } from "../utils/cameras.type";

function useCameraSelector(startCamera: Array<Cameras>) {
	const [sockets, setSockets] = useState<Array<WebSocket | undefined>>([undefined]);
	const [images, setImages] = React.useState<Array<string>>([""]);
	const [cameras, setCameras] = useState<Array<Cameras>>(startCamera);

	const setCamera = (camera: Cameras, select: boolean) => {
		setCameras((prevCameras) => {
			let newCameras = prevCameras.filter((cam) => cam !== camera);
			if (select) newCameras.push(camera);
			return newCameras;
		});
	};

	const setImage = (image: string, index: number) => {
		setImages((prevImages) => {
			let newImages = [...prevImages];
			newImages[index] = image;
			return newImages;
		});
	};

	const setSocket = (socket: WebSocket | undefined, index: number) => {
		setSockets((prevSockets) => {
			let newSockets = [...prevSockets];
			newSockets[index] = socket;
			return newSockets;
		});
	};

	const getCookie = (name: string): string | null => {
		let cookieValue = null;
		if (document.cookie && document.cookie !== "") {
			const cookies = document.cookie.split(";");
			for (let i = 0; i < cookies.length; i++) {
				const cookie = cookies[i].trim();
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) === name + "=") {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	};

	useEffect(() => {
		console.log("connect cam: " + cameras);

		for (const socket in sockets) {
			if (Object.prototype.hasOwnProperty.call(sockets, socket)) {
				const element = sockets[socket];
				if (element) element.onmessage = null;
			}
		}

		let newSockets: Array<WebSocket> = [];
		setImages(new Array(cameras.length).fill(null));

		for (let i = 0; i < cameras.length; i++) {
			const csrftoken = getCookie("csrftoken");
			let formData = new FormData();
			formData.append("index", cameras[i].toString());
			//formData.append('y',  y.toString());
			//formData.append('yaw', o.toString());

			let request = new Request("http://127.0.0.1:8000/csApp/cameras/enable_cameras", {
				method: "POST",
				headers: {
					"X-CSRFToken": csrftoken ?? "",
				},
				body: formData,
			});

			fetch(request)
				.then((res) => res.json())
				.then((data) => console.log(data))
				.catch((err) => console.log(err));

			let cameraSocket = new WebSocket(
				"ws://" + window.location.host + "/ws/cameras/" + "video" + cameras[i] + "/"
			);

			cameraSocket.onmessage = (e) => {
				const data = JSON.parse(e.data);
				console.log(data.data);
				setImage(data.data, i);
			};

			cameraSocket.onerror = (e) => {
				console.log(e);
				setSocket(undefined, i);
			};

			newSockets.push(cameraSocket);
		}

		setSockets(newSockets);
	}, [cameras]);

	const selectCamera = (camera: string, select = true) => {
		switch (camera) {
			case "Camera 1":
				setCamera(Cameras.CAM1, !(cameras.includes(Cameras.CAM1) && cameras.length > 1));
				break;
			case "Camera 2":
				setCamera(Cameras.CAM2, !(cameras.includes(Cameras.CAM2) && cameras.length > 1));
				break;
			case "Camera 3":
				setCamera(Cameras.CAM3, !(cameras.includes(Cameras.CAM3) && cameras.length > 1));
				break;
			case "Camera 4":
				setCamera(Cameras.CAM4, !(cameras.includes(Cameras.CAM4) && cameras.length > 1));
				break;
			case "Camera 5":
				setCamera(Cameras.CAM5, !(cameras.includes(Cameras.CAM5) && cameras.length > 1));
				break;
			case "Camera 6":
				setCamera(Cameras.CAM6, !(cameras.includes(Cameras.CAM6) && cameras.length > 1));
				break;
			default:
				setCamera(Cameras.NOCAM, select);
		}
	};

	return [images, cameras, selectCamera] as const;
}

export default useCameraSelector;
