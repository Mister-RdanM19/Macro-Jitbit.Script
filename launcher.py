import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# --- KONFIGURASI ---
NAMA_APLIKASI = "Macro Jitbit Script"
AUTHOR = "Mr.Rm19"
# Masukkan path file Jitbit kamu di sini
PATH_JITBIT_EXE = r"C:\Program Files (x86)\Jitbit Macro Recorder\MacroRecorder.exe"
PATH_SCRIPT_JMB = r"GB_PB_MrRm19.jmb" 

class MacroLauncher:
    def __init__(self, root):
        self.root = root
        self.root.title(f"{NAMA_APLIKASI} - {AUTHOR}")
        self.root.geometry("450x350")
        self.root.configure(bg="#121212")  # Dark Theme
        self.root.resizable(False, False)

        # --- HEADER ASCII / JUDUL ---
        self.header = tk.Label(
            root, 
            text="[ MR.RM19 ENGINE ]", 
            font=("Courier", 18, "bold"), 
            bg="#121212", 
            fg="#00FF41"  # Hacker Green
        )
        self.header.pack(pady=20)

        self.title_label = tk.Label(
            root, 
            text=NAMA_APLIKASI, 
            font=("Arial", 14, "bold"), 
            bg="#121212", 
            fg="#FFFFFF"
        )
        self.title_label.pack()

        self.line = tk.Label(root, text="_______________________________", bg="#121212", fg="#333333")
        self.line.pack(pady=5)

        # --- TOMBOL UTAMA ---
        self.btn_start = tk.Button(
            root, 
            text="START MACRO", 
            command=self.jalankan_macro,
            font=("Arial", 10, "bold"),
            bg="#1E1E1E",
            fg="#00FF41",
            activebackground="#00FF41",
            width=25,
            height=2,
            bd=1,
            relief="flat"
        )
        self.btn_start.pack(pady=10)

        self.btn_folder = tk.Button(
            root, 
            text="OPEN SCRIPT FOLDER", 
            command=self.buka_folder,
            font=("Arial", 10),
            bg="#1E1E1E",
            fg="#00BFFF", # Deep Sky Blue
            activebackground="#00BFFF",
            width=25,
            bd=1,
            relief="flat"
        )
        self.btn_folder.pack(pady=5)

        # --- FOOTER ---
        self.status_var = tk.StringVar(value="Status: Ready")
        self.status_label = tk.Label(
            root, 
            textvariable=self.status_var, 
            font=("Arial", 8), 
            bg="#121212", 
            fg="#888888"
        )
        self.status_label.pack(side="bottom", pady=10)

    def jalankan_macro(self):
        if os.path.exists(PATH_JITBIT_EXE):
            try:
                # Menjalankan Jitbit langsung dengan script jmb
                subprocess.Popen([PATH_JITBIT_EXE, PATH_SCRIPT_JMB])
                self.status_var.set("Status: Macro Running...")
            except Exception as e:
                messagebox.showerror("Error", f"Gagal menjalankan macro: {e}")
        else:
            messagebox.showwarning("Not Found", "Jitbit Launcher tidak ditemukan!\nPastikan path EXE sudah benar.")

    def buka_folder(self):
        os.startfile(os.getcwd())

if __name__ == "__main__":
    root = tk.Tk()
    app = MacroLauncher(root)
    root.mainloop()