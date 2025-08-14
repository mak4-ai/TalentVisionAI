import tkinter as tk
from tkinter import filedialog, messagebox
from ai_engine import filter_resumes
import os

def select_resumes():
    path = filedialog.askdirectory(title="Select Resumes Folder")
    if path:
        resumes_path.set(path)

def select_jd():
    file_path = filedialog.askopenfilename(title="Select Job Description File", filetypes=[("Text files", "*.txt")])
    if file_path:
        jd_path.set(file_path)

def select_output():
    path = filedialog.askdirectory(title="Select Output Folder")
    if path:
        output_path.set(path)

def run_ai():
    if not resumes_path.get() or not jd_path.get() or not output_path.get():
        messagebox.showerror("Error", "Please select all required paths!")
        return
    
    try:
        filter_resumes(resumes_path.get(), jd_path.get(), output_path.get())
        messagebox.showinfo("Success", f"Resumes filtered successfully!\nSaved in: {output_path.get()}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create window
root = tk.Tk()
root.title("TalentVisionAI - Resume Filter")
root.geometry("500x300")

# Variables
resumes_path = tk.StringVar()
jd_path = tk.StringVar()
output_path = tk.StringVar()

# GUI Elements
tk.Label(root, text="Resumes Folder:").pack(pady=5)
tk.Entry(root, textvariable=resumes_path, width=50).pack()
tk.Button(root, text="Browse", command=select_resumes).pack()

tk.Label(root, text="Job Description File:").pack(pady=5)
tk.Entry(root, textvariable=jd_path, width=50).pack()
tk.Button(root, text="Browse", command=select_jd).pack()

tk.Label(root, text="Output Folder:").pack(pady=5)
tk.Entry(root, textvariable=output_path, width=50).pack()
tk.Button(root, text="Browse", command=select_output).pack()

tk.Button(root, text="Run AI", command=run_ai, bg="green", fg="white", width=20).pack(pady=20)

root.mainloop()
