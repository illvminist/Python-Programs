import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("IT'S OVER!", "You must be retarded!")

# Create the main window
root = tk.Tk()
root.title("DEADLY BUTTON!!!!")
root.geometry("300x200")

# Create a button widget
button = tk.Button(root, text="BLOW IT ALL UP?", command=on_button_click)
button.pack(pady=20)
button2 = tk.Button(root, text="BLOW IT ALL UP MORE?", command=on_button_click)
button2.pack(pady=50)

# Run the application
root.mainloop()