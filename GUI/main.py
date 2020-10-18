import gi
import cv2

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, GdkPixbuf

class Main:
    def __init__(self):
    
	#CS styling setup
        screen = Gdk.Screen.get_default()
        provider = Gtk.CssProvider()
        style_context = Gtk.StyleContext()
        style_context.add_provider_for_screen(
            screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        
        #CSS script
        css = b"""
        #NAVBUTTON {
           border-radius: 35px;
           border: 5px solid #3464AB;
           
        }
        
        #SWITCH {
           border-radius: 360px;
           border: 5px solid red;
           background: #FD8080;
           
        }
        
        #Idle{
        
	color: #4797CD;
	font-weight: bold;
	font-size: 25px; 
	border: 5px solid #4797CD;
	background: #141C31 
        
        }
        
        #Idle:hover {
        background: white;
        
        }
        
        #Start{
        
	color: #0CEA13;
	font-weight: bold;
	font-size: 25px; 
	border: 5px solid #0CEA13;
	background: #141C31 
        
        }
        #Working{
        
	color: #EBDD1A;
	font-weight: bold;
	font-size: 25px; 
	border: 5px solid #EBDD1A;
	background: #141C31 
        
        }
        #Wait{
        
	color: #FCD306;
	font-weight: bold;
	font-size: 25px; 
	border: 5px solid #FCD306;
	background: #141C31 
        
        }
        #Waiting{
        
	color: #D2119D;
	font-weight: bold;
	font-size: 25px; 
	border: 5px solid #D2119D;
	background: #141C31 
        
        }
        #Resume{
        
	color: #2BAF17;
	font-weight: bold;
	font-size: 25px; 
	border: 5px solid #2BAF17;
	background: #141C31 
        
        }
        #Abort{
        
	color: #FA0F2F;
	font-weight: bold;
	font-size: 25px; 
	border: 5px solid #FA0F2F;
	background: #141C31 
        
        }
        
        
        #GRID {
           
           border: 2px solid #3464AB;
           
        }
        
        #CAMERA_LABEL {
        	color: white;
        	font-weight: bold;
        	border-bottom: 2px solid yellow;
        	border-left: 2px solid yellow;
        	border-right: 2px solid yellow;
        }
        
        #IMAGE {
           
           border-bottom: 2px solid #3464AB;
           
        }
        
        #label {
           background: #6C83B8;
           color: white;
           font-weight: bold;
           font-size: 28px; 
           border-top: 2px solid #3464AB; 
        }
        
        #LABEL4 {
           
           color: Red;
           font-weight: bold;
           font-size: 38px; 
           border: 10px solid red; 
        }
         #LABEL5 {
           
           color: Green;
           font-weight: bold;
           font-size: 38px; 
           border: 10px solid Green; 
        }
        
        #label2 {
           background: #141C31;
           border-bottom: 2px solid #3464AB;
        }
        
        #TAB_FRAME {
           background: #6C83B8;
        }
        
        #DATA_FRAME {
        border: 2px solid #3464AB;
        }
        
        #frame1 {
           background: #141C31;
        }
        """
        provider.load_from_data(css)
        
       


 #Camera setup
        
capture = cv2.VideoCapture(0)

capture.set(3, 500)
capture.set(4, 340)
       
def show_frame(*args):
	ret, frame = capture.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	
	framecp = frame.copy()
	
	pb=GdkPixbuf.Pixbuf.new_from_data(framecp.tobytes(), GdkPixbuf.Colorspace.RGB, False, 8, framecp.shape[1], framecp.shape[0], framecp.shape[2]*framecp.shape[1])
	
	image1.set_from_pixbuf(pb.copy())
	image2.set_from_pixbuf(pb.copy())
	
	return True
	
        
        
#Glade file setup
gladeFile = "Main.glade"
builder = Gtk.Builder()
builder.add_from_file(gladeFile)

#GUI Layout

window = builder.get_object("window1")
image1 = builder.get_object("image1")
image2 = builder.get_object("image2")
window.connect("delete-event", Gtk.main_quit)
window.show_all()
builder.connect_signals(Main())
GLib.idle_add(show_frame)   
        
       
##win = Main()
Gtk.main()
