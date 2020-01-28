#!/usr/bin/env python3

import gi
import os
import GUI
import subprocess
import threading
import webbrowser
import shutil

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf


class Main(Gtk.Window):
    def __init__(self):
        super(Main, self).__init__(title="Arcolinux Welcome App")
        self.set_border_width(10)
        # self.set_resizable(False)
        #self.set_size_request(750, 150)
        self.set_icon_from_file(os.path.join(
            GUI.base_dir, 'images/arcolinux.png'))
        self.set_position(Gtk.WindowPosition.CENTER)

        if not os.path.exists(GUI.home + "/.config/arcolinux-welcome-app/"):
            os.mkdir(GUI.home + "/.config/arcolinux-welcome-app/")
            with open(GUI.home + "/.config/arcolinux-welcome-app/settings.conf", "w") as f:
                f.write("autostart=True")
                f.close()

        GUI.GUI(self, Gtk, GdkPixbuf)

    def on_ai_clicked(self, widget):
        t = threading.Thread(target=self.run_app, args=(["pkexec /usr/bin/calamares"],))
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
            if os.path.isfile("/usr/share/applications/arcolinux-welocome-app.desktop"):
                shutil.copy("/usr/share/applications/arcolinux-welocome-app.desktop", GUI.home + "/.config/autostart/arcolinux-welocome-app.desktop")
        else:
            if os.path.isfile(GUI.home + "/.config/autostart/arcolinux-welocome-app.desktop"):
                os.unlink(GUI.home + "/.config/autostart/arcolinux-welocome-app.desktop")
        self.save_settings(widget.get_active())

    def save_settings(self, state):
        with open(GUI.home + "/.config/arcolinux-welcome-app/settings.conf", "w") as f:
            f.write("autostart=" + str(state))
            f.close()

    def load_settings(self):
        line = "False"
        with open(GUI.home + "/.config/arcolinux-welcome-app/settings.conf", "r") as f:
            lines = f.readlines()
            for i in range(len(lines)):
                if "autostart" in lines[i]:
                    line = lines[i].split("=")[1].rstrip().lstrip()
            f.close()
        return line

    def on_link_clicked(self, widget, link):
        webbrowser.open_new_tab(link)

    def on_social_clicked(self, widget, event, link):
        webbrowser.open_new_tab(link)

    def cb_allocate( self, label, allocation ):
        label.set_size_request( allocation.width - 2, -1 )

if __name__ == "__main__":
    w = Main()
    w.connect("delete-event", Gtk.main_quit)
    w.show_all()
    Gtk.main()
