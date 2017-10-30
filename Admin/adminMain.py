import os

if os.name == 'nt':
    import gi
    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk as gtk
else:
    import pygtk
    pygtk.require("2.0")
    import gtk

class APP:


    def __init__(self):
        #Constantes
        self.widList = []

        topwin = gtk.Window()
        topwin.connect('destroy',gtk.main_quit)
        
        label = gtk.Label('Administrador')
        topwin.add(label)

        self.widList.append(topwin)
        self.widList.append(label)
        self.showInit()

        gtk.main()

    def showInit(self):
        for w in self.widList:
            w.show()
        del self.widList
        
a = APP()
