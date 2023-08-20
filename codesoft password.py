import tkinter as tk
from tkinter import messagebox
import random
import string

def genpass():
    global passlen_entry, pass_entry
    try:
        passlen = int(passlen_entry.get())
        if passlen <= 0:
            raise ValueError("Password length must be a positive integer.")
        password_characters = string.ascii_letters + string.digits + string.punctuation
        generated_password = ''.join(random.choice(password_characters) for _ in range(passlen))
        pass_entry.delete(0, tk.END)
        pass_entry.insert(tk.END, generated_password)
        pass_entry.config(fg="Red")
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def accept_password():
    global username_entry, pass_entry
    username = username_entry.get()
    password = pass_entry.get()
    messagebox.showinfo("Accepted", f"Username: {username}\nPassword: {password}")

def reset_password():
    global username_entry, passlen_entry, pass_entry
    username_entry.delete(0, tk.END)
    passlen_entry.delete(0, tk.END)
    pass_entry.delete(0, tk.END)

def create_password_generator():
    global username_entry, passlen_entry, pass_entry
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("280x300")

    tk.Label(root, text="Password Generator", font=("Arial", 20, "underline"), bg="white", fg="darkblue").grid(row=0, columnspan=2, pady=10)

    tk.Label(root, text="Enter name: ").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
    username_entry = tk.Entry(root, justify="center")
    username_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

    tk.Label(root, text="Enter password length: ").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
    passlen_entry = tk.Entry(root, justify="center")
    passlen_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

    tk.Label(root, text="Generated password: ").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
    pass_entry = tk.Entry(root, justify="center")
    pass_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

    genpass_frame = tk.Frame(root, highlightthickness=2, highlightbackground="black",bg="darkblue")
    genpass_frame.grid(row=4, columnspan=2, pady=10)
    genpass_button = tk.Button(genpass_frame, text="Generate password", bg="darkblue", fg="white", bd=0, command=genpass)
    genpass_button.pack(pady=2, padx=10)

    accept_frame = tk.Frame(root, highlightthickness=2, highlightbackground="black")
    accept_frame.grid(row=5, columnspan=2, pady=5)
    accept_button = tk.Button(accept_frame, text="ACCEPT", bg="white", fg="darkblue", bd=0, command=accept_password)
    accept_button.pack(pady=2, padx=18)

    reset_frame = tk.Frame(root, highlightthickness=2, highlightbackground="black")
    reset_frame.grid(row=6, columnspan=2, pady=5)
    reset_button = tk.Button(reset_frame, text="RESET", bg="white", fg="darkblue", bd=0, command=reset_password)
    reset_button.pack(pady=2, padx=25)

    root.mainloop()

if __name__ == "__main__":
    create_password_generator()
