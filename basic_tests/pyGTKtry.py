import os

if os.name == 'nt':
    import gi
    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk as gtk

def create_window():
    window = gtk.Window()
    window.set_default_size(200, 200)
    window.connect('destroy', gtk.main_quit)

    label = gtk.Label('Hello World')
    window.add(label)

    label.show()
    window.show()

create_window()
gtk.main()
