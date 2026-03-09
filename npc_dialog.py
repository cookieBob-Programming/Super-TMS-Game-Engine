#!/usr/bin/env python3
"""
NPC Dialog - läuft als separater Prozess (tkinter + SDL Konflikt auf macOS 26)
"""
import tkinter as tk
import sys

def show_dialog():
    msg = sys.argv[1] if len(sys.argv) > 1 else "Hallo Abenteurer!"
    
    root = tk.Tk()
    root.title("NPC Dialog")
    root.geometry("400x200")
    root.resizable(False, False)
    
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(expand=True, fill="both")
    
    label = tk.Label(frame, text=msg, font=("Arial", 14), wraplength=360)
    label.pack(pady=20)
    
    btn = tk.Button(frame, text="OK", command=root.destroy, font=("Arial", 12), width=10)
    btn.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    show_dialog()
