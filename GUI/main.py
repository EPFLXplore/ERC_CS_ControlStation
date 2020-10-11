import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

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
        #button1 {
           background: yellow;
        }
        
        #label {
           background: #6C83B8;
           color: white;
           font-weight: bold;
           font-size: 28px 
        }
        
        #label2 {
           background: #13192F;
        }
        
        #frame1 {
           background: #13192F;
        }
        """
        provider.load_from_data(css)
        
        #Glade file setup
        gladeFile = "Main.glade"
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gladeFile)
      
	#GUI Layout
        ##button = self.builder.get_object("button1")
        window = self.builder.get_object("window1")
        window.connect("delete-event", Gtk.main_quit)
        window.show()
        
        
        
       
win = Main()
Gtk.main()
