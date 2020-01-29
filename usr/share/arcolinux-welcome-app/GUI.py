import os
import getpass
from os.path import expanduser

base_dir = os.path.dirname(os.path.realpath(__file__))
home = expanduser("~")
username = getpass.getuser()
user = "liveuser"

def GUI(self, Gtk, GdkPixbuf):

    autostart = eval(self.load_settings())


    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=15)
    self.add(vbox)

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    # hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    # vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    # vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    # ======================================================================
    #                   WELCOME LABEL
    # ======================================================================

    self.cc = Gtk.Label()

    label = Gtk.Label(xalign=0)
    label.set_markup(
        "<big>Welcome to <b>Arcolinux</b></big>")
    label.set_line_wrap(True)

    # pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(
    #     os.path.join(base_dir, 'images/arcolinux-one-liner.png'), 145, 145)
    # image = Gtk.Image().new_from_pixbuf(pixbuf)

    label2 = Gtk.Label(xalign=0)
    label2.set_justify(Gtk.Justification.CENTER)
    label2.set_line_wrap(True)

    if username == user:

        label2.set_markup(
            "We advise to clean  the computer with Gparted before installing. During the Calamares installation many options will be open to you. You have the freedom of choice. " +
    "The links below will get you started on ArcoLinux. We communicate with our community via a diversity of social media. Do join us to learn the latest news, ask questions or for casual talk. \n\n" +
    "We appreciate your feed-back and donation.  \nLearn, have fun and enjoy. \n\n" +
    "The ArcoLinux Team")
    else:
        label2.set_markup("The links below will get you started on ArcoLinux. We communicate with our community via a diversity of social media. Do join us to learn the latest news, ask questions or for casual talk. \n\n" +
    "We appreciate your feed-back and donation.  \nLearn, have fun and enjoy. \n\n" +
    "The ArcoLinux Team")
    # label2.connect( "size-allocate", self.cb_allocate )
    # vbox1.pack_start(image, False, False, 0)
    # vbox2.pack_start(label, False, False, 0)
    # vbox2.pack_start(label2, False, False, 0)
    hbox1.pack_start(label, False, False, 0)
    hbox1.pack_end(self.cc, False, False, 0)
    # hbox4.set_homogeneous(False)
    hbox4.pack_start(label2, False, False, 0)

    grid = Gtk.Grid()

    # ======================================================================
    #                   MAIN BUTTONS
    # ======================================================================

    button1 = Gtk.Button(label="")
    button1_label = button1.get_child()
    button1_label.set_markup("<span size='large'><b>Run GParted</b></span>")
    button1.connect("clicked", self.on_gp_clicked)
    button1.set_size_request(0, 100)

    button2 = Gtk.Button(label="")
    button2_label = button2.get_child()
    button2_label.set_markup("<span size='large'><b>Run Calamares</b></span>")

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

    button4 = Gtk.Button(label="Choose your project")
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

    button8 = Gtk.Button(label="Donate")
    button8.connect("clicked", self.on_link_clicked, "https://arcolinux.info/donation/")

    button9 = Gtk.Button(label="Get Involved")
    button9.connect("clicked", self.on_link_clicked, "https://arcolinux.info/looking-for-betatesters/")

    button10 = Gtk.Button(label="Debug")
    button10.connect("clicked", self.on_link_clicked, "https://github.com/arcolinux")

    button11 = Gtk.Button(label="Youtube")
    button11.connect("clicked", self.on_link_clicked, "https://www.youtube.com/erikdubois")

    hbox5.pack_start(button8, True, True, 0)
    hbox5.pack_start(button9, True, True, 0)
    hbox5.pack_start(button10, True, True, 0)
    hbox5.pack_start(button11, True, True, 0)

    # ======================================================================
    #                   Add to startup
    # ======================================================================
    check = Gtk.CheckButton(label="Start on Startup")
    check.connect("toggled", self.statup_toggle)
    check.set_active(autostart)
    hbox3.pack_end(check, False, False, 0)

    # ======================================================================
    #                   SOCIAL LINKS
    # ======================================================================
    fbE = Gtk.EventBox()
    tE = Gtk.EventBox()
    meE = Gtk.EventBox()
    inE = Gtk.EventBox()
    liE = Gtk.EventBox()
    pE = Gtk.EventBox()
    dE = Gtk.EventBox()
    tgE = Gtk.EventBox()

    pbfb = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/facebook.png'), 28, 28)
    fbimage = Gtk.Image().new_from_pixbuf(pbfb)

    pbt = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/twitter.png'), 28, 28)
    timage = Gtk.Image().new_from_pixbuf(pbt)

    pbme = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/mewe.png'), 23, 23)
    meimage = Gtk.Image().new_from_pixbuf(pbme)

    pbin = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/insta.png'), 28, 28)
    inimage = Gtk.Image().new_from_pixbuf(pbin)

    pbli = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/linkedin.png'), 28, 28)
    liimage = Gtk.Image().new_from_pixbuf(pbli)

    pbp = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/patreon.png'), 28, 28)
    pimage = Gtk.Image().new_from_pixbuf(pbp)

    pbd = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/discord.png'), 28, 28)
    dimage = Gtk.Image().new_from_pixbuf(pbd)

    pbtg = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/tg.png'), 28, 28)
    tgimage = Gtk.Image().new_from_pixbuf(pbtg)

    fbE.add(fbimage)
    tE.add(timage)
    meE.add(meimage)
    inE.add(inimage)
    liE.add(liimage)
    pE.add(pimage)
    dE.add(dimage)
    tgE.add(tgimage)

    fbE.connect("button_press_event", self.on_social_clicked, "https://www.facebook.com/groups/arcolinux")
    tE.connect("button_press_event", self.on_social_clicked, "https://twitter.com/arcolinux")
    meE.connect("button_press_event", self.on_social_clicked, "https://mewe.com/group/5bbc4577a40f3002b313671d")
    inE.connect("button_press_event", self.on_social_clicked, "https://www.instagram.com/arcolinux/")
    liE.connect("button_press_event", self.on_social_clicked, "https://www.linkedin.com/in/arcolinux/")
    pE.connect("button_press_event", self.on_social_clicked, "https://www.patreon.com/arcolinux")
    dE.connect("button_press_event", self.on_social_clicked, "https://discordapp.com/invite/R2amEEz")
    tgE.connect("button_press_event", self.on_social_clicked, "https://t.me/arcolinux_d_b")

    fbE.set_property("has-tooltip", True)
    tE.set_property("has-tooltip", True)
    meE.set_property("has-tooltip", True)
    inE.set_property("has-tooltip", True)
    liE.set_property("has-tooltip", True)
    pE.set_property("has-tooltip", True)
    dE.set_property("has-tooltip", True)
    tgE.set_property("has-tooltip", True)

    fbE.connect("query-tooltip", self.tooltip_callback, "Facebook")
    tE.connect("query-tooltip", self.tooltip_callback, "Twitter")
    meE.connect("query-tooltip", self.tooltip_callback, "Mewe")
    inE.connect("query-tooltip", self.tooltip_callback, "Instagram")
    liE.connect("query-tooltip", self.tooltip_callback, "LinkedIn")
    pE.connect("query-tooltip", self.tooltip_callback, "Patreon")
    dE.connect("query-tooltip", self.tooltip_callback, "Discord")
    tgE.connect("query-tooltip", self.tooltip_callback, "Telegram")


    hbox3.pack_start(fbE, False, False, 0)
    hbox3.pack_start(tE, False, False, 0)
    hbox3.pack_start(meE, False, False, 0)
    hbox3.pack_start(inE, False, False, 0)
    hbox3.pack_start(liE, False, False, 0)
    hbox3.pack_start(pE, False, False, 0)

    hbox6.pack_start(dE, False, False, 0)
    hbox6.pack_start(tgE, False, False, 0)
    hbox3.pack_start(hbox6, True, False, 0)

    # ======================================================================
    #                   PACK TO WINDOW
    # ======================================================================



    vbox.pack_start(hbox1, False, False, 0)  # Logo
    vbox.pack_start(hbox4, False, False, 0)  # welcome Label

    if username == user:
        vbox.pack_start(grid, True, False, 0)  # Run GParted
    vbox.pack_end(hbox3, False, False, 0)  # Footer
    vbox.pack_end(hbox5, False, False, 0)  # Buttons
    vbox.pack_end(hbox2, False, False, 0)  # Buttons
