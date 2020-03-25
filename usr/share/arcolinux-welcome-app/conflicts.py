import gi
import os
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk  # noqa

base_dir = os.path.dirname(os.path.realpath(__file__))


class Conflicts(Gtk.Window):
    def __init__(self, title="AWA Conflicts"):
        super(Conflicts, self).__init__()
        self.set_border_width(10)
        self.set_default_size(550, 250)
        self.connect("delete-event", self.close)
        self.set_icon_from_file(os.path.join(base_dir, 'images/arcolinux.png'))
        self.set_position(Gtk.WindowPosition.CENTER)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(vbox)

        # If you want header in middle then remove xalign=0
        lblh1 = Gtk.Label(xalign=0)
        lblh1.set_markup("<b><i>HEADER 1</i></b>")

        lblh2 = Gtk.Label(xalign=0)
        lblh2.set_markup("<b><i>HEADER 2</i></b>")

        lblh3 = Gtk.Label(xalign=0)
        lblh3.set_markup("<b><i>HEADER 2</i></b>")

        lblh4 = Gtk.Label(xalign=0)
        lblh4.set_markup("<b><i>HEADER 2</i></b>")

        lblh5 = Gtk.Label(xalign=0)
        lblh5.set_markup("<b><i>HEADER 2</i></b>")

        lblm1 = Gtk.Label()
        lblm1.set_text("App #1 conflicts with App #2")

        lblm2 = Gtk.Label()
        lblm2.set_text("App #1 conflicts with App #2")

        lblm3 = Gtk.Label()
        lblm3.set_text("App #1 conflicts with App #2")

        lblm4 = Gtk.Label()
        lblm4.set_text("App #1 conflicts with App #2")

        lblm5 = Gtk.Label()
        lblm5.set_text("App #1 conflicts with App #2")

        vbox.pack_start(lblh1, False, False, 0)
        vbox.pack_start(lblm1, False, False, 0)

        vbox.pack_start(lblh2, False, False, 0)
        vbox.pack_start(lblm2, False, False, 0)

        vbox.pack_start(lblh3, False, False, 0)
        vbox.pack_start(lblm3, False, False, 0)

        vbox.pack_start(lblh4, False, False, 0)
        vbox.pack_start(lblm4, False, False, 0)

        vbox.pack_start(lblh5, False, False, 0)
        vbox.pack_start(lblm5, False, False, 0)

    def close(self, widget, event):
        self.destroy()
