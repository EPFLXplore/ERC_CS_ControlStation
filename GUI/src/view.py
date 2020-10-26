import gi
import cv2

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GLib, GdkPixbuf
'''
	@author Emile Hreich

	View Class (MVC)


	@Attributes
		controller -> Controller

'''
class View:

	#Constructor
	def __init__(self, controller):

		self.controller = controller
		screen = Gdk.Screen.get_default()
		provider = Gtk.CssProvider()
		style_context = Gtk.StyleContext()
		style_context.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
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
        #Start:hover {
          background: white;
        
        }
        #Working:hover {
          background: white;
        
        }
        #Wait:hover {
          background: white;
        
        }
        #Resume:hover {
          background: white;
        
        }
        #Abort:hover {
          background: white;
        
        }
        #Waiting:hover {
          background: white;
        
        }
        #SWITCH:hover{
          background : #FFA9A9;
        }
        #SWITCH:active{
          background : #FD8080;
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
        
        #Tab-Label {
           background: #6C83B8;
           color: white;
           font-weight: bold;
           font-size: 28px; 
           border-top: 2px solid #3464AB; 
        }
        
        #AUTO {
           
           color: Red;
           font-weight: bold;
           font-size: 38px; 
           border: 10px solid red; 
        }
         #MANUAL {
           
           color: Green;
           font-weight: bold;
           font-size: 38px; 
           border: 10px solid Green; 
        }
        
        #Window_Top {
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
        #LABEL_MD {
           color: white;
           font-weight: bold;
           font-size: 25px;
        }
        #LABEL_SM {
           color: white;
           font-weight: bold;
           font-size: 15px;
        }
        """
		provider.load_from_data(css)
		self.capture = cv2.VideoCapture(0)
		self.capture.set(3, 500)
		self.capture.set(4, 340)
		#Glade file setup
		gladeFile = "Main.glade"
		builder = Gtk.Builder()
		builder.add_from_file(gladeFile)
		#GUI Layout
		self.window = builder.get_object("window1")
		self.window2 = builder.get_object("window2")
		self.image1 = builder.get_object("image1")
		self.image2 = builder.get_object("image2")



	def show_frame(self, *args):
		self.ret, self.frame = self.capture.read()
		self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
		
		framecp = self.frame.copy()
		
		pb=GdkPixbuf.Pixbuf.new_from_data(framecp.tobytes(), GdkPixbuf.Colorspace.RGB, False, 8, framecp.shape[1], framecp.shape[0], framecp.shape[2]*framecp.shape[1])
		
		self.image1.set_from_pixbuf(pb.copy())
		self.image2.set_from_pixbuf(pb.copy())
		
		return True





