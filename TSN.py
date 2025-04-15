import tkinter as tk
import os
from datetime import datetime
import platform

def save_text(event=None):
    note = TextField.get("1.0", tk.END)
    date = datetime.now().strftime("%d/%m,%Y, %H:%M:%S")
    note_with_date = f"{date} {note}\n"
    with open(home_path, "a") as file:
        file.write(note_with_date)
    TextField.delete("1.0", tk.END)

Frame = tk.Tk()
Frame.title("Truly Small Notes")
Frame.geometry("410x470")
Frame.resizable(height=False,width=False)
Frame.config(bg="white")

MainFrame = tk.Frame(master=Frame, height=280, width=300, bg="white", relief="solid", bd=5)
MainFrame.pack(fill="both", expand=True)

TextField = tk.Text(MainFrame, height=20, width=40, bg="#f5f5f5", fg="black", font=("Helvetica", 12), bd=2, wrap="word", relief="flat")
TextField.pack(side="top", pady=5, padx=5)

home_dir = os.path.expanduser("~")
home_path = os.path.join(home_dir, "Desktop", "note.txt")
Save = tk.Button(
    MainFrame,
    text="Save",
    command=save_text,
    bg="#ff66b2",
    fg="Black",
    font=("Helvetica", 12, "bold"),
    relief="flat",
    bd=1.5,
    width=12,
    height=2
)
Save.pack(side="bottom")

Frame.bind("<Return>", save_text)

if platform.system() == "Darwin":
    Frame.bind("<Command-S>", save_text)
else:
    Frame.bind("<Control-S>", save_text)

Frame.mainloop()