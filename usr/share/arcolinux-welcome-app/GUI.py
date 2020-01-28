import os
import getpass
from os.path import expanduser

base_dir = os.path.dirname(os.path.realpath(__file__))
home = expanduser("~")
username = getpass.getuser()

def GUI(self, Gtk, GdkPixbuf):
    autostart = eval(self.load_settings())

    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
    self.add(vbox)

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    # ======================================================================
    #                   WELCOME LABEL
    # ======================================================================

    label = Gtk.Label(xalign=0)
    label.set_markup(
        "<big>Welcome to <b>Arcolinux</b></big>")
    label.set_line_wrap(True)

    pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/arcolinux-one-liner.png'), 145, 145)
    image = Gtk.Image().new_from_pixbuf(pixbuf)

    label2 = Gtk.Label(xalign=0)    
    label2.set_text(
        "Follow the steps below to get started installing <b>Arcolinux</b>\nsomething something else and more on that subject later today :D")
    label2.set_line_wrap(True)
    
    # hbox4.pack_start(label2, False, False, 0)
    vbox2.pack_start(label, True, False, 0)
    vbox2.pack_start(label2, True, False, 0)
    hbox1.pack_start(image, False, False, 0)
    hbox1.pack_end(vbox2, False, False, 0)


    grid = Gtk.Grid()
    grid2 = Gtk.Grid()
     
    # ======================================================================
    #                   MAIN BUTTONS
    # ======================================================================

    if username == "liveuser":
        button1 = Gtk.Button(label="Run GParted")
        button1.connect("clicked", self.on_gp_clicked)
        button1.set_size_request(0, 100)

        button2 = Gtk.Button(label="Run Arcolinux Installer")
        button2.connect("clicked", self.on_ai_clicked)
        button2.set_size_request(0, 100)

        grid.add(button1)
        grid.attach(button1, 0, 0, 1, 2)
        grid.attach(button2, 1, 0, 1, 2)
    grid.set_column_homogeneous(True)
    # grid.set_row_homogeneous(True)


    # ======================================================================
    #                   FOOTER BUTTON LINKS
    # ======================================================================
    button3 = Gtk.Button(label="Release info")
    button3.connect("clicked", self.on_link_clicked, "https://arcolinux.info/category/2020/")
    
    button4 = Gtk.Button(label="choose your project")
    button4.connect("clicked", self.on_link_clicked, "https://arcolinux.info/choose-your-project/")

    button5 = Gtk.Button(label="Core info")
    button5.connect("clicked", self.on_link_clicked, "https://arcolinux.info/arcolinux-editions/")
    
    button6 = Gtk.Button(label="Fast track")
    button6.connect("clicked", self.on_link_clicked, "https://arcolinux.info/fast-track/")

    button7 = Gtk.Button(label="Forum")
    button7.connect("clicked", self.on_link_clicked, "http://arcolinuxforum.com/")
      
    hbox2.pack_start(button3, True, True, 0)
    hbox2.pack_start(button4, True, True, 0)
    hbox2.pack_start(button5, True, True, 0)
    hbox2.pack_start(button6, True, True, 0)
    hbox2.pack_start(button7, True, True, 0)

    # ======================================================================
    #                   Add to startup
    # ======================================================================
    check = Gtk.CheckButton(label="Start on Startup")
    check.connect("toggled", self.statup_toggle)
    check.set_active(autostart)
    hbox3.pack_end(check, False, False, 0)
    
    # ======================================================================
    #                   PACK TO WINDOW
    # ======================================================================

    

    vbox.pack_start(hbox1, False, False, 0)  # welcome Label
    vbox.pack_start(hbox4, False, False, 0)  # welcome Label
    vbox.pack_start(grid, True, False, 0)  # Run GParted    
    vbox.pack_start(hbox2, False, False, 0)  # Run Installer
    vbox.pack_start(hbox3, False, False, 0)  # Run Installer
