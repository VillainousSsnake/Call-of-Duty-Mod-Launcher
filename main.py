# /main.py
# runs app

# Importing libraries
import os.path
from tkinter import filedialog as fd
from custom_lib.config import Config
from pyunpack import Archive
import tkinter as tk
import ctypes as ct
import subprocess
import hashlib
import shutil


# App Functions
def generate_hash(mod_file_name):
    hash_object = hashlib.sha256(mod_file_name.encode())
    hex_dig = hash_object.hexdigest()
    return str(hex_dig)


# Creating the root window
root = tk.Tk()
root.title("Call of Duty: Mod Launcher")
root.geometry("500x500+200+200")
root.configure(bg="#131642")
root.resizable(False, True)

# Making the title bar dark mode
root.update()
ct.windll.dwmapi.DwmSetWindowAttribute(ct.windll.user32.GetParent(root.winfo_id()), 20, ct.byref(ct.c_int(2)),
                                       ct.sizeof(ct.c_int(2)))


# Defining on_close function
def on_close():
    root.destroy()


# Assigning the on_close function to the exit button on root
root.protocol("WM_DELETE_WINDOW", on_close)


# uninstallAllModsButton command
def uninstall_all_mods_button_command():
    pass  # TODO: Stub


# installModButton command
def install_mod_button_command():

    # Ask for the file
    modFilePath = fd.askopenfilename()

    # Extract it into _temp_/*mod_hash*
    mod_hash = generate_hash(os.path.join(modFilePath))
    Archive(modFilePath).extractall(os.path.join(os.getcwd(), "_temp_", mod_hash))

    # Copy and replace it into Call of Duty Location
    source_directory = os.path.join(os.getcwd(), "_temp_", mod_hash)
    destination_directory = 'destination_directory'

    shutil.copytree(source_directory, destination_directory)


# launchButton command
def launch_button_command():
    current_game_exe_path = Config.get_entry_value("current_game_path")
    if os.path.exists(current_game_exe_path):
        subprocess.run(current_game_exe_path)


# Creating launchButton
launchButton = tk.Button(root,
                         text="Launch",
                         command=launch_button_command,
                         width=30,
                         font="2px",
                         bg="#8b41bf", borderwidth=2,
                         highlightcolor="#ba75eb")

# Creating injectButton
uninstallModsButton = tk.Button(root,
                                text="Uninstall All Mods",
                                command=uninstall_all_mods_button_command,
                                width=30,
                                font="2px",
                                bg="#8b41bf", borderwidth=2,
                                highlightcolor="#ba75eb")

# Creating installModsButton
installModButton = tk.Button(root,
                             text="Install Mod",
                             command=install_mod_button_command,
                             width=30,
                             font="2px",
                             bg="#8b41bf", borderwidth=2,
                             highlightcolor="#ba75eb")

# Packing buttons
launchButton.pack(side="bottom")
uninstallModsButton.pack(side="bottom")
installModButton.pack(side="bottom")


# Root window mainloop
root.mainloop()
