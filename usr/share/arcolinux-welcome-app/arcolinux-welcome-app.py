#!/usr/bin/env python3
# =================================================================
# =                  Author: Brad Heffernan                       =
# =================================================================
import gi
import os
import GUI
import subprocess
import threading
import webbrowser
import shutil
import socket
from time import sleep
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, GLib  # noqa

REMOTE_SERVER = "www.google.com"


class Main(Gtk.Window):
    def __init__(self):
        super(Main, self).__init__(title="ArcoLinux Welcome App")
        self.set_border_width(10)
        self.set_default_size(750, 250)
        self.set_icon_from_file(os.path.join(
            GUI.base_dir, 'images/arcolinux.png'))
        self.set_position(Gtk.WindowPosition.CENTER)
        self.results = ""
        if not os.path.exists(GUI.home + "/.config/arcolinux-welcome-app/"):
            os.mkdir(GUI.home + "/.config/arcolinux-welcome-app/")
            with open(GUI.Settings, "w") as f:
                f.write("autostart=True")
                f.close()

        GUI.GUI(self, Gtk, GdkPixbuf)

        if GUI.username == GUI.user:
            t = threading.Thread(target=self.internet_notifier, args=())
            t.daemon = True
            t.start()

    def on_ai_clicked(self, widget):
        t = threading.Thread(target=self.run_app,
                             args=(["pkexec", "/usr/bin/calamares"],))
        t.daemon = True
        t.start()

    def on_gp_clicked(self, widget):
        t = threading.Thread(target=self.run_app,
                             args=(["/usr/bin/gparted"],))
        t.daemon = True
        t.start()

    def run_app(self, command):
        subprocess.call(command,
                        shell=False,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

    def statup_toggle(self, widget):
        if widget.get_active() is True:
            if os.path.isfile(GUI.dot_desktop):
                shutil.copy(GUI.dot_desktop, GUI.autostart)
        else:
            if os.path.isfile(GUI.autostart):
                os.unlink(GUI.autostart)
        self.save_settings(widget.get_active())

    def save_settings(self, state):
        with open(GUI.Settings, "w") as f:
            f.write("autostart=" + str(state))
            f.close()

    def load_settings(self):
        line = "True"
        if os.path.isfile(GUI.Settings):
            with open(GUI.Settings, "r") as f:
                lines = f.readlines()
                for i in range(len(lines)):
                    if "autostart" in lines[i]:
                        line = lines[i].split("=")[1].strip().capitalize()
                f.close()
        return line

    def on_link_clicked(self, widget, link):
        t = threading.Thread(target=self.weblink, args=(link,))
        t.daemon = True
        t.start()

    def on_social_clicked(self, widget, event, link):
        t = threading.Thread(target=self.weblink, args=(link,))
        t.daemon = True
        t.start()

    def weblink(self, link):
        webbrowser.open_new_tab(link)

    def is_connected(self):
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            s = socket.create_connection((host, 80), 2)
            s.close()
            return True
        except:  # noqa
            pass
        return False

    def tooltip_callback(self, widget, x, y, keyboard_mode, tooltip, text):
        tooltip.set_text(text)
        return True

    def on_launch_clicked(self, widget, event, link):
        if os.path.isfile("/usr/local/bin/arcolinux-tweak-tool"):
            t = threading.Thread(target=self.run_app,
                                 args=("/usr/local/bin/arcolinux-tweak-tool",))
            t.daemon = True
            t.start()
        else:
            md = Gtk.MessageDialog(parent=self,
                                   flags=0,
                                   message_type=Gtk.MessageType.INFO,
                                   buttons=Gtk.ButtonsType.YES_NO,
                                   text="Not Found!")
            md.format_secondary_markup(
                "<b>ArcoLinux Tweak Tool</b> was not found on your system\n\
Do you want to install it?")

            result = md.run()

            md.destroy()

            if result in (Gtk.ResponseType.OK, Gtk.ResponseType.YES):
                t1 = threading.Thread(target=self.installATT, args=())
                t1.daemon = True
                t1.start()

    def internet_notifier(self):
        while(True):
            if not self.is_connected():
                GLib.idle_add(self.cc.set_markup, "<span foreground='orange'><b><i>Not connected to internet</i></b> \nCalamares will <b>not</b> install additional software</span>")  # noqa
            else:
                GLib.idle_add(self.cc.set_text, "")
            sleep(3)

    def MessageBox(self, title, message):
        md = Gtk.MessageDialog(parent=self,
                               flags=0,
                               message_type=Gtk.MessageType.INFO,
                               buttons=Gtk.ButtonsType.OK,
                               text=title)
        md.format_secondary_markup(message)
        md.run()
        md.destroy()

    def installATT(self):
        subprocess.call(["pkexec",
                         "/usr/bin/pacman",
                         "-S",
                         "arcolinux-tweak-tool-git",
                         "--noconfirm"], shell=False)
        GLib.idle_add(self.MessageBox,
                      "Success!",
                      "<b>ArcoLinux Tweak Tool</b> has been installed successfully")  # noqa
    # def get_message(self, title, message):
    #     t = threading.Thread(target=self.fetch_notice,
#                              args=(title, message,))
    #     t.daemon = True
    #     t.start()
    #     t.join()

    # def fetch_notice(self, title, message):
    #     try:
    #         url = 'https://bradheff.github.io/notice/notice'
    #         req = requests.get(url, verify=True, timeout=1)

    #         if req.status_code == requests.codes.ok:
    #             if not len(req.text) <= 1:
    #                 title.set_markup(
    #                 "<big><b><u>Notice</u></b></big>")
    #                 message.set_markup(req.text)
    #                 self.results = True
    #             else:
    #                 self.results = False
    #         else:
    #             self.results = False
    #     except:
    #         self.results = False


if __name__ == "__main__":
    w = Main()
    w.connect("delete-event", Gtk.main_quit)
    w.show_all()
    Gtk.main()
