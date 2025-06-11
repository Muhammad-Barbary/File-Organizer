import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import PhotoImage

class FileOrganizerGUI:
    def __init__(self, master):
        self.master = master
        master.title("File Organizer")

        self.label = tk.Label(master, text="Select a directory to organize:")
        self.label.pack(pady=10)

        self.directory_entry = tk.Entry(master, width=50)
        self.directory_entry.pack(pady=5)

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_directory)
        self.browse_button.pack(pady=5)

        self.organize_button = tk.Button(master, text="Organize Files", command=self.organize_files)
        self.organize_button.pack(pady=20)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory_entry.delete(0, tk.END)
            self.directory_entry.insert(0, directory)

    def organize_files(self):
        target_dir = self.directory_entry.get().strip()
        if not os.path.isdir(target_dir):
            messagebox.showerror("Error", "Invalid directory.")
            return
        
        try:
            for item in os.listdir(target_dir):
                item_path = os.path.join(target_dir, item)
                if os.path.isfile(item_path):
                    _, ext = os.path.splitext(item)
                    category = self.get_category(ext)
                    dest_folder = os.path.join(target_dir, category)
                    self.ensure_folder(dest_folder)
                    unique_name = self.get_unique_filename(dest_folder, item)
                    dest_path = os.path.join(dest_folder, unique_name)
                    shutil.move(item_path, dest_path)
                    print(f"Moved: {item} -> {category}/{unique_name}")
            messagebox.showinfo("Success", "Files organized successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def get_category(self, extension):
        FILE_CATEGORIES = {
            "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
            "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
            "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
            "Video": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
            "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
            "Scripts": [".py", ".js", ".sh", ".bat", ".rb"],
            "Others": []
        }
        for category, extensions in FILE_CATEGORIES.items():
            if extension.lower() in extensions:
                return category
        return "Others"

    def ensure_folder(self, path):
        if not os.path.exists(path):
            os.makedirs(path)

    def get_unique_filename(self, dest_folder, filename):
        base, ext = os.path.splitext(filename)
        counter = 1
        new_filename = filename
        while os.path.exists(os.path.join(dest_folder, new_filename)):
            new_filename = f"{base} ({counter}){ext}"
            counter += 1
        return new_filename

if __name__ == "__main__":
    root = tk.Tk()
    icon = PhotoImage(file='src/icon.png')
    root.iconphoto(True, icon)
    gui = FileOrganizerGUI(root)
    root.mainloop()