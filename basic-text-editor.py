from tkinter import *
from tkinter import filedialog

def new_file():
    text_area.delete("1.0", END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as file:
            text = file.read()
            text_area.delete("1.0", END)
            text_area.insert("1.0", text)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            text = text_area.get("1.0", END)
            file.write(text)

def save_file_as():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w") as file:
            text = text_area.get("1.0", END)
            file.write(text)

root = Tk()
root.title("Text Editor")
root.geometry("800x600")

menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_file_as)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

text_area = Text(root)
text_area.pack(fill=BOTH, expand=YES)

root.mainloop()
