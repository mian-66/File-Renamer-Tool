# Pro Renamer Utility 📂

A lightweight, professional desktop application built in Python to batch-rename files instantly. Say goodbye to renaming hundreds of files by hand!

## 🚀 Features

* **Live Preview:** See exactly what your new filenames will look like as you type, before making any changes.
* **Smart Patterns:**
  * **Sequence:** Number files automatically (e.g., `File1`, `File2`, `File3`).
  * **Prefix & Suffix:** Add text to the beginning or end of your files.
  * **Replace Text:** Find specific words or characters and replace them across all files.
  * **Case Swap:** Instantly convert filenames to UPPERCASE or lowercase.
* **Safe & Secure:** Built-in error handling ensures you don't accidentally overwrite files or use illegal Windows characters.

## 📥 How to Download & Run (For Users)

You do not need Python installed to run this app!

1. Go to the [Releases](../../releases/latest) tab on the right side of this page.
2. Download the `ProRenamer.exe` file.
3. Double-click to run! (Note: Windows may show a "Protected your PC" warning. Click **More Info** -> **Run Anyway**).

## 💻 How to Run from Source (For Developers)

If you want to run the raw Python code or build the executable yourself:

1. **Clone this repository:**
   ```bash
   git clone https://https://github.com/mian-66/File-Renamer-Tool.git
   ```

2. **Install the required libraries:**
   ```bash
   pip install customtkinter
   ```

3. **Run the script:**
   ```bash
   python renamer_app.py
   ```

---

## 🛠️ Built With
- **Python 3**
- **CustomTkinter** (Modern GUI framework)
- **PyInstaller** (Standalone executable packaging)
