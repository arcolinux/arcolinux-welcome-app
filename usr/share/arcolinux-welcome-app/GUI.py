# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================

import os
import getpass
from os.path import expanduser

DEBUG = False
base_dir = os.path.dirname(os.path.realpath(__file__))
home = expanduser("~")
username = getpass.getuser()

if DEBUG:
    user = username
else:
    user = "liveuser"

Settings = home + "/.config/arcolinux-welcome-app/settings.conf"
Skel_Settings = "/etc/skel/.config/arcolinux-welcome-app/settings.conf"
dot_desktop = "/usr/share/applications/arcolinux-welcome-app.desktop"
autostart = home + "/.config/autostart/arcolinux-welcome-app.desktop"


def GUI(self, Gtk, GdkPixbuf):

    autostart = eval(self.load_settings())

    self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    self.add(self.vbox)

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox5 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox6 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox7 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox8 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    # vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    # vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    infoE = Gtk.EventBox()
    pbinfo = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/question.png'), 38, 38)
    infoimage = Gtk.Image().new_from_pixbuf(pbinfo)
    infoE.add(infoimage)
    infoE.connect("button_press_event", self.on_info_clicked)
    infoE.set_property("has-tooltip", True)
    infoE.connect("query-tooltip", self.tooltip_callback, "Conflicts Info")

    # ======================================================================
    #                   WELCOME LABEL
    # ======================================================================

    self.cc = Gtk.Label()

    label = Gtk.Label(xalign=0)
    label.set_markup(
        "<big>Welcome to <b>ArcoLinux</b></big>")
    label.set_line_wrap(True)

    # pixbuf = GdkPixbuf.Pixbuf().new_from_file_at_size(
    #     os.path.join(base_dir, 'images/arcolinux-one-liner.png'), 145, 145)
    # image = Gtk.Image().new_from_pixbuf(pixbuf)

    label2 = Gtk.Label(xalign=0)
    label2.set_justify(Gtk.Justification.CENTER)
    label2.set_line_wrap(True)

    if username == user:

        label2.set_markup(
            "We advise to clean the computer with Gparted before installing. During the Calamares installation many options will be open to you. You have the freedom of choice. " +  # noqa
            "The links below will get you started on ArcoLinux. We communicate with our community via a diversity of social media. Do join us to learn the latest news, ask questions or for casual talk. \n\n" +  # noqa
            "We appreciate your feed-back and donation.  \nLearn, have fun and enjoy. \n\n" +  # noqa
            "The ArcoLinux Team")
    else:
        label2.set_markup("The links below will get you started on ArcoLinux. We communicate with our community via a diversity of social media. Do join us to learn the latest news, ask questions or for casual talk. \n\n" +  # noqa
                          "We appreciate your feed-back and donation.  \nLearn, have fun and enjoy. \n\n" +  # noqa
                          "The ArcoLinux Team")
    # label2.connect( "size-allocate", self.cb_allocate )
    # vbox1.pack_start(image, False, False, 0)
    # vbox2.pack_start(label, False, False, 0)
    # vbox2.pack_start(label2, False, False, 0)
    hbox1.pack_start(label, False, False, 0)
    hbox1.pack_end(self.cc, False, False, 0)
    # hbox4.set_homogeneous(False)
    hbox4.pack_start(label2, False, False, 0)

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

    self.button8 = Gtk.Button(label="")
    button8_label = self.button8.get_child()
    button8_label.set_markup("<span size='large'><b>Update Arch Linux mirrors</b></span>")
    self.button8.connect("clicked", self.on_mirror_clicked)
    self.button8.set_size_request(210, 70)

    button13 = Gtk.Button(label="")
    button13_label = button13.get_child()
    button13_label.set_markup("<span size='large'><b>ArcoLinux Calamares Tool</b></span>")
    button13.connect("clicked", self.on_arcolinux_calamares_tool_clicked)
    button13.set_size_request(210, 70)

    # grid.add(button1)
    if username == user:
        grid = Gtk.Grid()
        grid.attach(self.button8, 0, 0, 2, 2)
        grid.attach(button13, 2, 0, 2, 2)
        grid.attach(button1, 0, 2, 2, 2)
        grid.attach(button2, 2, 2, 2, 2)
        grid.set_column_homogeneous(True)
    else:
        grid = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.button8.set_size_request(420, 70)
        grid.pack_start(self.button8, True, False, 0)
    # grid.set_row_homogeneous(True)

    # ======================================================================
    #                   NOTICE
    # ======================================================================

    # label3 = Gtk.Label(xalign=0)
    # label3.set_line_wrap(True)

    # label4 = Gtk.Label(xalign=0)
    # label4.set_line_wrap(True)

    # self.vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    # self.vbox2.pack_start(label3, False,False,0)
    # self.vbox2.pack_start(label4, False,False,0)

    # ======================================================================
    #                   USER INFO
    # ======================================================================

    lblusrname = Gtk.Label(xalign=0)
    lblusrname.set_text("User:")

    lblpassword = Gtk.Label(xalign=0)
    lblpassword.set_text("Pass:")

    lblusr = Gtk.Label(xalign=0)
    lblusr.set_text("liveuser  |")

    lblpass = Gtk.Label(xalign=0)
    lblpass.set_markup("<i>No Password</i>")

    hboxUser = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    hboxUser.pack_start(lblusrname, False, False, 0)
    hboxUser.pack_start(lblusr, False, False, 0)

    hboxUser.pack_start(lblpassword, False, False, 0)
    hboxUser.pack_start(lblpass, False, False, 0)

    # ======================================================================
    #                   FOOTER BUTTON LINKS
    # ======================================================================
    button3 = Gtk.Button(label="Release info")
    button3.connect("clicked", self.on_link_clicked,
                    "https://arcolinux.info/releases-2021/")

    button4 = Gtk.Button(label="Choose your project")
    button4.connect("clicked", self.on_link_clicked,
                    "https://arcolinux.info/choose-your-project/")

    button5 = Gtk.Button(label="Core info")
    button5.connect("clicked", self.on_link_clicked,
                    "https://arcolinux.info/arcolinux-editions/")

    button6 = Gtk.Button(label="Fast track")
    button6.connect("clicked", self.on_link_clicked,
                    "https://arcolinux.info/fast-track/")

    button7 = Gtk.Button(label="Forum")
    button7.connect("clicked", self.on_link_clicked,
                    "http://arcolinuxforum.com/")

    hbox2.pack_start(button3, True, True, 0)
    hbox2.pack_start(button4, True, True, 0)
    hbox2.pack_start(button5, True, True, 0)
    hbox2.pack_start(button6, True, True, 0)
    hbox2.pack_start(button7, True, True, 0)

    button8 = Gtk.Button(label="")
    button8_label = button8.get_child()
    button8_label.set_markup("<b>Donate</b>")
    button8.connect("clicked", self.on_link_clicked,
                    "https://arcolinux.info/donation/")

    button9 = Gtk.Button(label="Get Involved")
    button9.connect("clicked", self.on_link_clicked,
                    "https://arcolinux.info/looking-for-betatesters/")

    button10 = Gtk.Button(label="Debug")
    button10.connect("clicked", self.on_link_clicked,
                     "https://github.com/arcolinux")

    button11 = Gtk.Button(label="Youtube")
    button11.connect("clicked", self.on_link_clicked,
                     "https://www.youtube.com/erikdubois")

    button12 = Gtk.Button(label="Quit")
    button12.set_size_request(200, 50)
    button12.connect("clicked", Gtk.main_quit)
    #button12.set_tooltip_markup("Quit the ArcoLinux Welcome App")

    hbox5.pack_start(button8, True, True, 0)
    hbox5.pack_start(button9, True, True, 0)
    hbox5.pack_start(button10, True, True, 0)
    hbox5.pack_start(button11, True, True, 0)
    hbox5.pack_start(button12, True, True, 0)


    # hbox8.pack_start(self.button8, True, False, 0)

    # ======================================================================
    #                   Add to startup
    # ======================================================================

    check = Gtk.CheckButton(label="Autostart")
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

    fbE.connect("button_press_event", self.on_social_clicked,
                "https://www.facebook.com/groups/arcolinux")
    tE.connect("button_press_event", self.on_social_clicked,
               "https://twitter.com/arcolinux")
    meE.connect("button_press_event", self.on_social_clicked,
                "https://mewe.com/group/5bbc4577a40f3002b313671d")
    inE.connect("button_press_event", self.on_social_clicked,
                "https://www.instagram.com/arcolinux/")
    liE.connect("button_press_event", self.on_social_clicked,
                "https://www.linkedin.com/in/arcolinux/")
    pE.connect("button_press_event", self.on_social_clicked,
               "https://www.patreon.com/arcolinux")
    dE.connect("button_press_event", self.on_social_clicked,
               "https://discordapp.com/invite/R2amEEz")
    tgE.connect("button_press_event", self.on_social_clicked,
                "https://t.me/arcolinux_d_b")

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
    if username == user:
        hbox3.pack_start(hboxUser, True, False, 0)
    hbox3.pack_start(hbox6, True, False, 0)

    # ======================================================================
    #                   Start Arcolinux Tweak Tool
    # ======================================================================
    launchBox = Gtk.EventBox()
    pblaunch = GdkPixbuf.Pixbuf().new_from_file_at_size(
        os.path.join(base_dir, 'images/hefftor.svg'), 40, 40)
    launchimage = Gtk.Image().new_from_pixbuf(pblaunch)

    launchBox.add(launchimage)
    launchBox.connect("button_press_event", self.on_launch_clicked, "")

    launchBox.set_property("has-tooltip", True)
    launchBox.connect("query-tooltip",
                      self.tooltip_callback,
                      "Run Arcolinux Tweak Tool")

    hbox6.pack_start(launchBox, False, False, 0)
    hbox6.pack_start(infoE, False, False, 0)
    # ======================================================================
    #                   PACK TO WINDOW
    # ======================================================================
    label3 = Gtk.Label("v20.6-4")
    hbox7.pack_end(label3, False, False, 0)
    # if self.is_connected():
    #     self.get_message(label3, label4)

    self.vbox.pack_start(hbox1, False, False, 7)  # Logo
    self.vbox.pack_start(hbox4, False, False, 7)  # welcome Label

    self.vbox.pack_start(grid, True, False, 7)  # Run GParted/Calamares

    # if self.results and self.is_connected():
    #     self.vbox.pack_start(self.vbox2, False, False, 0)  # Notice

    self.vbox.pack_end(hbox3, False, False, 0)  # Footer
    #self.vbox.pack_end(hbox7, False, False, 0)  # Version
    self.vbox.pack_end(hbox5, False, False, 7)  # Buttons
    self.vbox.pack_end(hbox2, False, False, 7)  # Buttons
