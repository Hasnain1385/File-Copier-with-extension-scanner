import os
import shutil
import tkinter as tk
from tkinter import filedialog, ttk, messagebox


class FileCopyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Copy with Directory Structure")
        
        # Initialize variables
        self.source_dir = tk.StringVar()
        self.target_dir = tk.StringVar()
        self.selected_extension = tk.StringVar()
        self.extensions = []

        # Build GUI
        self.create_widgets()

    def create_widgets(self):
        # Source directory selection
        tk.Label(self.root, text="Source Directory:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(self.root, textvariable=self.source_dir, width=50).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_source).grid(row=0, column=2, padx=5, pady=5)

        # Scan button
        tk.Button(self.root, text="Scan Directory", command=self.scan_directory).grid(row=1, column=1, padx=5, pady=5)

        # Dropdown for file extensions
        tk.Label(self.root, text="Select Extension:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.extension_dropdown = ttk.Combobox(self.root, textvariable=self.selected_extension, state="readonly")
        self.extension_dropdown.grid(row=2, column=1, padx=5, pady=5)

        # Target directory selection
        tk.Label(self.root, text="Target Directory:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        tk.Entry(self.root, textvariable=self.target_dir, width=50).grid(row=3, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_target).grid(row=3, column=2, padx=5, pady=5)

        # Copy button
        tk.Button(self.root, text="Copy Files", command=self.copy_files).grid(row=4, column=1, padx=5, pady=5)

    def browse_source(self):
        directory = filedialog.askdirectory()
        if directory:
            self.source_dir.set(directory)

    def browse_target(self):
        directory = filedialog.askdirectory()
        if directory:
            self.target_dir.set(directory)

    def scan_directory(self):
        source = self.source_dir.get()
        if not os.path.isdir(source):
            messagebox.showerror("Error", "Please select a valid source directory.")
            return

        self.extensions = self.get_file_extensions(source)
        self.extension_dropdown['values'] = self.extensions
        if self.extensions:
            self.extension_dropdown.current(0)
        messagebox.showinfo("Scan Complete", f"Found {len(self.extensions)} unique file extensions.")

    def get_file_extensions(self, directory):
        extensions = set()
        for root, _, files in os.walk(directory):
            for file in files:
                _, ext = os.path.splitext(file)
                if ext:  # Only include files with extensions
                    extensions.add(ext.lower())
        return sorted(extensions)

    def copy_files(self):
        source = self.source_dir.get()
        target = self.target_dir.get()
        extension = self.selected_extension.get()

        if not os.path.isdir(source):
            messagebox.showerror("Error", "Please select a valid source directory.")
            return
        if not os.path.isdir(target):
            messagebox.showerror("Error", "Please select a valid target directory.")
            return
        if not extension:
            messagebox.showerror("Error", "Please select a file extension.")
            return

        self.copy_files_with_extension(source, target, extension)
        messagebox.showinfo("Copy Complete", "Files copied successfully!")

    def copy_files_with_extension(self, source, target, extension):
        for root, _, files in os.walk(source):
            for file in files:
                if file.endswith(extension):
                    relative_path = os.path.relpath(root, source)
                    target_path = os.path.join(target, relative_path)

                    # Create target directories if they don't exist
                    os.makedirs(target_path, exist_ok=True)

                    # Copy file
                    shutil.copy2(os.path.join(root, file), os.path.join(target_path, file))


if __name__ == "__main__":
    root = tk.Tk()
    app = FileCopyApp(root)
    root.mainloop()
