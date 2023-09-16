import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def show_about_popup():
        about_popup = tk.Toplevel(root)
        about_popup.title("About")
        about_popup.geometry("300x100")

        about_label = tk.Label(about_popup, text="Levi's text editor, PyEdit made in a basement. :)")
        about_label.pack(padx=10, pady=10)

        ok_button = tk.Button(about_popup, text="Ok", command=about_popup.destroy)
        ok_button.pack(pady=10)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))

def toggle_word_wrap():
    if word_wrap.get() == 1:
        text.config(wrap=tk.WORD)
    else:
        text.config(wrap=tk.NONE)

def resize_text(event):
    text.config(font=("Calibri", font_size.get()))

root = tk.Tk()
root.title("PyEdit")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

view_menu = tk.Menu(menu)
menu.add_cascade(label="View", menu=view_menu)
word_wrap = tk.IntVar()
view_menu.add_checkbutton(label="Word Wrap", variable=word_wrap, command=toggle_word_wrap)
font_size = tk.IntVar()
font_size.set(12)
view_menu.add_command(label="Resize Text", command=lambda: resize_text(None))

about_menu = tk.Menu(menu)
menu.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="About PyEdit", command=show_about_popup)

text = tk.Text(root)
text.pack(fill=tk.BOTH, expand=True)

text.bind("<Configure>", resize_text)

root.mainloop()
