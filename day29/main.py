import tkinter as tk
from tkinter import messagebox
import random
import json

letters = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F',
           'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L',
           'M', 'm', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R',
           's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x',
           'X', 'y', 'Y', 'z', 'Z']
sym_num = ["?", "!", "/", "%", "$", "&", ".", "#", "*", "+", "1",
           "2", "3", "4", "5", "6", "7", "8", "9", "0"]

# ---------------------------- PASSWORD GENERATOR ------------------------- #


def password_gen():
    entry_password.delete(first=0, last="end")
    password = [random.choice(letters) for _ in range(random.randint(10, 15))]
    password += [random.choice(sym_num) for _ in range(random.randint(4, 7))]

    random.shuffle(password)
    new = "".join(password)
    entry_password.insert(0, new)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_button_clicked():
    if len(entry_password.get()) > 0 and len(entry_website.get()) > 0 \
            and len(entry_user.get()) > 0:
        ok = messagebox.askokcancel(title=entry_website.get(),
                                    message="These are the details entered:\n"
                                    f"Email/Username: {entry_user.get()}\n"
                                    f"Password: {entry_password.get()}")

        if ok:
            with open("day29/my_passwords.json", "a") as f:
                dicta = {"Website": entry_website.get(),
                         "Email/Username": entry_user.get(),
                         "Password": entry_password.get()}
                f.write(json.dumps(dicta, indent=4,))
                f.write("\n")
            entry_password.delete(first=0, last="end")
            entry_website.delete(first=0, last="end")
    else:
        messagebox.askokcancel(title="Oops",
                               message="Don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #


window = tk.Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)


logo = tk.PhotoImage(file="day29/logo.png")
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

label_website = tk.Label(text="Website:")
label_website.grid(column=0, row=1)

label_user = tk.Label(text="Email/Username:")
label_user.grid(column=0, row=2)

lable_password = tk.Label(text="Password:")
lable_password.grid(column=0, row=3)

entry_website = tk.Entry(width=53)
entry_website.focus()
entry_website.grid(column=1, row=1, columnspan=2, padx=2, pady=2)

entry_user = tk.Entry(width=53)
entry_user.insert(0, "alfrvo@gmail.com")
entry_user.grid(column=1, row=2, columnspan=2, padx=2, pady=2)

entry_password = tk.Entry(width=33)
entry_password.grid(column=1, row=3, padx=2, pady=2)

button_generate = tk.Button(text="Generate Password", command=password_gen)
button_generate.grid(column=2, row=3, padx=2, pady=2)

button_add = tk.Button(text="Add", width=45, command=add_button_clicked)
button_add.grid(column=1, row=4, columnspan=2, padx=2, pady=2)


window.mainloop()
