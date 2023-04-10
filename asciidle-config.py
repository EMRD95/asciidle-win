import os
import tkinter as tk
from tkinter import filedialog, messagebox
import sys

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

        # Position the color picker window close to the pick color button
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
        
        # Add a new button to call the add_to_path method
        self.add_to_path_button = tk.Button(master, text="Add asciidle to PATH", command=self.add_to_path)
        self.add_to_path_button.grid(row=4, columnspan=3)

        self.entry_speed = tk.Entry(master, width=10)
        self.entry_speed.grid(row=2, column=1, sticky="W")

        self.save_button = tk.Button(master, text="Save", command=self.save_config)
        self.save_button.grid(row=3, columnspan=3)

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
                    key = winreg.OpenKey(
                        winreg.HKEY_CURRENT_USER,
                        "Environment",
                        access=winreg.KEY_ALL_ACCESS,
                    )
                    winreg.SetValueEx(key, "PATH", 0, winreg.REG_EXPAND_SZ, new_path)
                    winreg.CloseKey(key)
                    messagebox.showinfo("Success", "Asciidle added to PATH")
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
                self.entry_speed.insert(0, lines[5].strip
                ().strip())
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
    gui = AsciidleConfigEditor(root)
    root.mainloop()
