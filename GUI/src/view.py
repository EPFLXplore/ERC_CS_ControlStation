import gi
import cv2
import cairo

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

		#SC{
			color: #BEFF00;
			font-weight: bold;
			font-size: 15px;
			border: 5px solid #BEFF00;

		}
		#WE{
			color: #00FFD7;
        	font-weight: bold;
        	font-size: 15px;
        	border: 5px solid #00FFD7;

		}
		#CI{
			color:#CF00FF;
        	font-weight: bold;
        	font-size: 15px;
        	border: 5px solid #CF00FF;

		}
		#SP{
			color: #FF0037;
        	font-weight: bold;
        	font-size: 15px;
        	border: 5px solid #FF0037;

		}
		#CA{
			color: #FFB800;
        	font-weight: bold;
        	font-size: 15px;
        	border: 5px solid #FFB800;

		}

        #NAVBUTTON {
           border-radius: 35px;
           border: 5px solid #3464AB;

        }
        #NAVBUTTON_CURRENT {
           border-radius: 35px;
           border: 5px solid Red;

        }
        #SEPARATOR {

           background-color: #1CEBD6;

        }
		#SEPARATOR_2{
			background-color: #8e9ea3
		}

        #SWITCH {
           border-radius: 360px;
           border: 5px solid #49bf28;
           background: #83d16d;

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
          background : #b8e3ac;
        }
        #SWITCH:active{
          background : #83d16d;
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
        	border-bottom: 2px solid #3464AB;
        	border-left: 2px solid #3464AB;
        	border-right: 2px solid #3464AB;
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
		   border-radius: 20px
        }
		#AUTO_2 {

           color: Red;
           font-weight: bold;
           font-size: 18px;
           border: 10px solid red;
		   border-radius: 20px
        }
		#HD_LABEL{
			color: white;

			font-size: 12px;
			border: 3px solid white;
			border-radius: 20px;
		}
         #MANUAL {

           color: Green;
           font-weight: bold;
           font-size: 38px;
           border: 10px solid Green;
		   border-radius: 20px;
        }
         #MANUAL_2 {

           color: Green;
           font-weight: bold;
           font-size: 18px;
           border: 10px solid Green;
		   border-radius: 20px;
        }
		#SET{
			color: Green;
			font-weight: bold;
			font-size: 18px;
			border: 5px solid Green;
			border-radius: 360px;
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
        #DATA_FRAME_2 {
        	border: 2px solid #00FFD7;
        	border-radius : 10px;
        }
		#DATA_FRAME_3{
			border: 5px dashed #00FFD7;
        	border-radius : 360px;
		}
		#DATA_FRAME_4{
			border: 5px solid yellow;
        	background: #6C83B8;
		}
		#DATA_FRAME_6{
			background-image: url("../resources/HD2.png");
			background-repeat: no-repeat;
			background-position: bottom;
		}
		#TUBE_BUTTON{
			border-radius: 360px;
			color: white;
            font-weight: bold;
            background: #3464AB;
		}
        #DATA_FRAME_BG {

	        background-image: url("../resources/t.png");
	        background-repeat: no-repeat;
	        background-position: center;
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
		#DATA_LABEL_SM{
			color: #e8da1a;
            font-weight: bold;
            font-size: 15px;
		}
		#DATA_LABEL_MD{
			color: #e8da1a;
            font-weight: bold;
            font-size: 25px;
		}
		#DATA_COMPASS{
			background-image: url("../resources/compass.png");
	        background-repeat: no-repeat;
	        background-position: center;
		}
        """

		provider.load_from_data(css)
		self.capture = cv2.VideoCapture(0)
		self.capture.set(3, 500)
		self.capture.set(4, 340)
		#Glade file setup
		gladeFile = "Main.glade"
		self.builder = Gtk.Builder()
		self.builder.add_from_file(gladeFile)
		#GUI Layout
		self.window = self.builder.get_object("window1")
		self.window2 = self.builder.get_object("window2")

		self.image1 = self.builder.get_object("image1")
		self.image2 = self.builder.get_object("image2")

		self.battery = self.builder.get_object("battery")
		#self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, self.builder.get_object("compass").get_allocated_width(), self.builder.get_object("compass").get_allocated_height())

	def show_frame(self, *args):

		self.ret, self.frame = self.capture.read()
		self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)

		framecp = self.frame.copy()

		pb=GdkPixbuf.Pixbuf.new_from_data(framecp.tobytes(), GdkPixbuf.Colorspace.RGB, False, 8, framecp.shape[1], framecp.shape[0], framecp.shape[2]*framecp.shape[1])

		self.image1.set_from_pixbuf(pb.copy())
		self.image2.set_from_pixbuf(pb.copy())

		return True
