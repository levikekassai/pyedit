import tkinter as tk
from tkinter import messagebox

def show_about_popup():
    about_popup = tk.Toplevel(root)
    about_popup.title("About")
    about_popup.geometry("300x100")

    about_label = tk.Label(about_popup, text="This is a sample About popup.")
    about_label.pack(padx=10, pady=10)

    ok_button = tk.Button(about_popup, text="OK", command=about_popup.destroy)
    ok_button.pack(pady=10)

root = tk.Tk()
root.title("Sample App")

menu = tk.Menu(root)
root.config(menu=menu)

about_menu = tk.Menu(menu)
menu.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="Show About", command=show_about_popup)

root.mainloop()
