#!/usr/bin/env python3

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
from gi.repository import Gtk, GdkPixbuf, GLib

REMOTE_SERVER = "www.google.com"

class Main(Gtk.Window):
    def __init__(self):
        super(Main, self).__init__(title="Arcolinux Welcome App")
        self.set_border_width(10)
        self.set_default_size(750, 250)
        self.set_icon_from_file(os.path.join(
            GUI.base_dir, 'images/arcolinux.png'))
        self.set_position(Gtk.WindowPosition.CENTER)

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
        t = threading.Thread(target=self.run_app, args=(["pkexec","/usr/bin/calamares"],))
        t.daemon = True
        t.start()

    def on_gp_clicked(self, widget):
        t = threading.Thread(target=self.run_app, args=(["/usr/bin/gparted"],))
        t.daemon = True
        t.start()

    def run_app(self, command):
        subprocess.call(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def statup_toggle(self, widget):
        if widget.get_active() == True:
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
        with open(GUI.Settings, "r") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if "autostart" in lines[i]:
                    line = lines[i].split("=")[1].rstrip().lstrip().capitalize()
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
        except:
            pass
        return False

    def tooltip_callback(self, widget, x, y, keyboard_mode, tooltip, text):
        tooltip.set_text(text)
        return True

    def internet_notifier(self):
        while(True):
            if not self.is_connected():
                GLib.idle_add(self.cc.set_markup, "<span foreground='orange'>Not connected to internet \nCalamares will not install additional software</span>")
            else:
                GLib.idle_add(self.cc.set_text,"")
            sleep(3)

if __name__ == "__main__":
    w = Main()
    w.connect("delete-event", Gtk.main_quit)
    w.show_all()
    Gtk.main()
