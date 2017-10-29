import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk as gtk

class Base:
    def __init__(self):
        self.window = gtk.Window() 
        #self.window = gtk.Window(gtk.WINDOW_TOPLEVEL) 
        self.window.show()
def main(self):
    gtk.main()
    #print __name__
if __name__ == "__main__":
    base = Base()
