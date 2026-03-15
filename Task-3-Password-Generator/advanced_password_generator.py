import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Length must be positive!")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter valid length!")
        return

    characters = ""

    if letters_var.get():
        characters += string.ascii_letters
    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation

    exclude_chars = exclude_entry.get()
    characters = ''.join(c for c in characters if c not in exclude_chars)

    if not characters:
        messagebox.showerror("Error", "Select at least one character type!")
        return

    # Strong password rule: ensure at least one of each selected type
    password = []
    
    if letters_var.get():
        password.append(random.choice(string.ascii_letters))
    if numbers_var.get():
        password.append(random.choice(string.digits))
    if symbols_var.get():
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    result = ''.join(password[:length])

    password_entry.delete(0, tk.END)
    password_entry.insert(0, result)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# ---- GUI ----
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x400")

tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack()

letters_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

tk.Checkbutton(root, text="Include Letters", variable=letters_var).pack()
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).pack()

tk.Label(root, text="Exclude Characters (optional):").pack()
exclude_entry = tk.Entry(root)
exclude_entry.pack()

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=10)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack()

root.mainloop()
