import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Define file type categories and their extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Video": [".mp4", ".mov", ".avi", ".mkv", ".wmv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".sh", ".bat", ".rb"],
    "Others": []
}

def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return "Others"

def ensure_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_unique_filename(dest_folder, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    while os.path.exists(os.path.join(dest_folder, new_filename)):
        new_filename = f"{base} ({counter}){ext}"
        counter += 1
    return new_filename

def organize_files(directory):
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            _, ext = os.path.splitext(item)
            category = get_category(ext)
            dest_folder = os.path.join(directory, category)
            ensure_folder(dest_folder)
            unique_name = get_unique_filename(dest_folder, item)
            dest_path = os.path.join(dest_folder, unique_name)
            shutil.move(item_path, dest_path)
            print(f"Moved: {item} -> {category}/{unique_name}")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        organize_files(directory)
        messagebox.showinfo("Success", "Files organized successfully!")

def create_gui():
    root = tk.Tk()
    root.title("File Organizer")
    root.geometry("300x150")

    label = tk.Label(root, text="File Organizer", font=("Helvetica", 16))
    label.pack(pady=20)

    organize_button = tk.Button(root, text="Select Directory", command=select_directory)
    organize_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_gui()