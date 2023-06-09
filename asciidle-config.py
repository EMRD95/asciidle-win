import os
import tkinter as tk
from tkinter import filedialog, messagebox, PhotoImage
import sys
import ctypes

class ANSIColorPicker(tk.Toplevel):
    ANSI_COLORS = {
        "30": "#000000",
        "31": "#800000",
        "32": "#008000",
        "33": "#808000",
        "34": "#000080",
        "35": "#800080",
        "36": "#008080",
        "37": "#C0C0C0",
        "90": "#808080",
        "91": "#FF0000",
        "92": "#00FF00",
        "93": "#FFFF00",
        "94": "#0000FF",
        "95": "#FF00FF",
        "96": "#00FFFF",
        "97": "#FFFFFF"
    }

    def __init__(self, master, callback, pick_color_button):
        super().__init__(master)
        self.callback = callback
        self.title("ANSI Color Picker")
        self.create_color_buttons()

        # Set the custom icon for the Tkinter window
        self.iconbitmap("res/asciidle-config.ico")

        x = pick_color_button.winfo_rootx() + pick_color_button.winfo_width()
        y = pick_color_button.winfo_rooty()
        self.geometry(f"+{x}+{y}")

    def create_color_buttons(self):
        buttons_per_row = 4
        for idx, (code, color) in enumerate(ANSIColorPicker.ANSI_COLORS.items()):
            button = tk.Button(self, bg=color, width=2, height=1, command=lambda c=code: self.select_color(c))
            button.grid(row=idx // buttons_per_row, column=idx % buttons_per_row)

    def select_color(self, color_code):
        self.callback(color_code)
        self.destroy()

class AsciidleConfigEditor:
    def __init__(self, master):
        self.master = master
        master.title("Asciidle Config Editor")

        self.label_path = tk.Label(master, text="ASCII Art Folder:")
        self.label_path.grid(row=0, column=0, sticky="W")

        self.entry_path = tk.Entry(master, width=40)
        self.entry_path.grid(row=0, column=1)

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_folder)
        self.browse_button.grid(row=0, column=2)

        self.label_color = tk.Label(master, text="Color Code:")
        self.label_color.grid(row=1, column=0, sticky="W")

        self.entry_color = tk.Entry(master, width=10)
        self.entry_color.grid(row=1, column=1, sticky="W")

        self.pick_color_button = tk.Button(master, text="Pick Color", command=self.pick_color)
        self.pick_color_button.grid(row=1, column=2)

        self.label_speed = tk.Label(master, text="Scroll Latency:")
        self.label_speed.grid(row=2, column=0, sticky="W")

        self.entry_speed = tk.Entry(master, width=10)
        self.entry_speed.grid(row=2, column=1, sticky="W")

        self.save_button = tk.Button(master, text="Save", command=self.save_config)
        self.save_button.grid(row=6, columnspan=3)

        # Create a button for downloading stuffs
        self.download_stuffs_button = tk.Button(master, text="Download ASCII art", command=self.download_stuffs)
        self.download_stuffs_button.grid(row=5, column=0, columnspan=2, sticky="W")

     # Load the shield icon
        self.admin_shield_image = PhotoImage(file="res/admin_shield.png")

        # Create a button with text and the shield icon
        self.add_to_path_button = tk.Button(master, text="Add asciidle to PATH ", command=self.add_to_path,
                                            image=self.admin_shield_image, compound="right")
        self.add_to_path_button.grid(row=4, column=0, columnspan=2, sticky="W", pady=3)

        self.load_config()


    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.entry_path.delete(0, tk.END)
            self.entry_path.insert(0, folder)

    def pick_color(self):
        color_picker = ANSIColorPicker(self.master, self.set_color, self.pick_color_button)

    def set_color(self, color_code):
        self.entry_color.delete(0, tk.END)
        self.entry_color.insert(0, color_code)

    def download_stuffs(self):
        def download_option(option):
            if option == "small":
                os.system("download-ascii-art.bat")
            elif option == "large":
                os.system("download-ascii-art2.bat")
            download_dialog.destroy()

        download_dialog = tk.Toplevel(self.master)
        download_dialog.title("Download Options")

        # Set the custom icon for the Tkinter window
        download_dialog.iconbitmap("res/asciidle-config.ico")

        small_set_button = tk.Button(download_dialog, text="Add a small set of pinups (NSFW, 500KB)", command=lambda: download_option("small"))
        small_set_button.pack(fill=tk.X, padx=5, pady=5)

        large_set_button = tk.Button(download_dialog, text="Add large set of random Ascii art (NSFW and unsorted, 16MB)", command=lambda: download_option("large"))
        large_set_button.pack(fill=tk.X, padx=5, pady=5)

        
    def add_to_path(self):
        script_path = os.path.abspath(sys.argv[0])
        script_folder = os.path.dirname(script_path)

        path_variable = os.environ.get("PATH", "")
        path_folders = path_variable.split(os.pathsep)

        if script_folder not in path_folders:
            path_folders.append(script_folder)
            new_path = os.pathsep.join(path_folders)

            if sys.platform == "win32":
                import winreg

                try:
                    # Check for administrator privileges
                    if ctypes.windll.shell32.IsUserAnAdmin():
                        # Add to system PATH
                        key = winreg.OpenKey(
                            winreg.HKEY_LOCAL_MACHINE,
                            r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment",
                            access=winreg.KEY_ALL_ACCESS,
                        )
                        winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
                        winreg.CloseKey(key)
                    else:
                        ctypes.windll.shell32.ShellExecuteW(
                            None, "runas", sys.executable, " ".join(sys.argv), None, 1
                        )
                        sys.exit()

                    # Add to user PATH
                    user_key = winreg.OpenKey(
                        winreg.HKEY_CURRENT_USER,
                        r"Environment",
                        access=winreg.KEY_ALL_ACCESS,
                    )
                    winreg.SetValueEx(user_key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
                    winreg.CloseKey(user_key)
                    messagebox.showinfo("Success", "Asciidle added to PATH for local user and admin. Note that it might require refreshing the variable environment or a restart for changes to take effect.y")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to add Asciidle to PATH: {e}")
            else:
                messagebox.showerror("Error", "Adding Asciidle to PATH is only supported on Windows")
        else:
            messagebox.showinfo("Info", "Asciidle is already in PATH")


    def load_config(self):
        try:
            with open("asciidle.cf", "r") as file:
                lines = file.readlines()
                self.entry_path.delete(0, tk.END)
                self.entry_path.insert(0, lines[1].strip())
                self.entry_color.delete(0, tk.END)
                self.entry_color.insert(0, lines[3].strip())
                self.entry_speed.delete(0, tk.END)
                self.entry_speed.insert(0, lines[5].strip().strip())
        except FileNotFoundError:
            messagebox.showerror("Error", "asciidle.cf not found")

    def save_config(self):
        with open("asciidle.cf", "w") as file:
            file.write("# Path for the ASCII art txt files\n")
            file.write(self.entry_path.get() + "\n")
            file.write("# Color code (use ANSI color escape codes)\n")
            file.write(self.entry_color.get() + "\n")
            file.write("# Scroll speed (less is more)\n")
            file.write(self.entry_speed.get() + "\n")
        messagebox.showinfo("Success", "Config saved")

if __name__ == "__main__":
    root = tk.Tk()
    
    # Set the custom icon for the Tkinter window
    root.iconbitmap("res/asciidle-config.ico")
    
    gui = AsciidleConfigEditor(root)
    root.mainloop()
