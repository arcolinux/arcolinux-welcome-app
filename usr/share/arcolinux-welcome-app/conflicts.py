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
        lblh1.set_markup("<b><i>Conflict 1</i></b>")

        lblm1 = Gtk.Label()
        lblm1.set_text("xcursor-breeze conflicts with breeze")

        lblh2 = Gtk.Label(xalign=0)
        lblh2.set_markup("<b><i>Conflict 2</i></b>")

        lblm2 = Gtk.Label()
        lblm2.set_text("visual-studio-code-bin conflicts with code")

        lblh3 = Gtk.Label(xalign=0)
        lblh3.set_markup("<b><i>Conflict3</i></b>")

        lblm3 = Gtk.Label()
        lblm3.set_text("synapse conflicts with catfish and zeitgeist")

        lblh4 = Gtk.Label(xalign=0)
        lblh4.set_markup("<b><i>Choose</i></b>")

        lblm4 = Gtk.Label()
        lblm4.set_text("Either choose libreoffice-fresh or libreoffice-still")

        lblh5 = Gtk.Label(xalign=0)
        lblh5.set_markup("<b><i>Choose</i></b>")

        lblm5 = Gtk.Label()
        lblm5.set_text("Either choose <b>virtualbox</b> for linux or linux-lts")


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
