# File Copier with Extension Scanner

This Python application allows users to copy files with specific extensions from a source directory (and its subdirectories) to a target directory while preserving the original directory structure. It features a user-friendly GUI built with `tkinter`, enabling users to scan directories, select file extensions from a dropdown, and efficiently copy files.

---

## Features

- **Scan Source Directory**: Detects all unique file extensions in the selected folder and its subfolders.
- **Dropdown for File Extensions**: Allows users to select a specific extension to filter files for copying.
- **Preserve Directory Structure**: Copies files to the target directory while maintaining the original folder hierarchy.
- **Simple GUI**: Easy-to-use interface with intuitive buttons for browsing, scanning, and copying.

---

## How to Use

1. **Select Source Directory**  
   Browse and choose the folder containing files to scan.

2. **Scan Directory**  
   Click the **Scan Directory** button to find all file extensions in the source directory.

3. **Select Extension**  
   Choose the desired file extension from the dropdown.

4. **Select Target Directory**  
   Browse and set the destination folder.

5. **Copy Files**  
   Click the **Copy Files** button to copy all files with the selected extension to the target folder.

---

## Prerequisites

- **Python 3.x**
- Standard libraries:
  - `os`
  - `shutil`
  - `tkinter`

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/file-copy-app.git
   cd file-copy-app
