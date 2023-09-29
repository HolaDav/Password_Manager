from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(numbers) for n in range(randint(2, 4))]
    password_list += [choice(symbols) for s in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get().title()
    email_username = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }
    }

    if len(website) < 1 or len(password) < 1:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_okay = messagebox.askokcancel(title="website", message=f"These are the details entered: "
                                                                  f"\nEmail: {email_username}\nPassword: "
                                                                  f"{password}\nIs is ok to save?")
        if is_okay:
            try:
                with open("data.json", mode="r") as file:
                    data = json.load(file)
                    data.update(new_data)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ----------------------------------SEARCH--------------------------------------- #


def find_password():
    website = website_entry.get().title()
    try:
        with open("data.json", "r") as file:
            web_search = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data file found")
    else:
        if website in web_search:
            messagebox.showinfo(title=f"{website}", message=f"Email: {web_search[website]['email']}\n"
                                                            f"Password: {web_search[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists")
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=52)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, "oladejidavid12@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

mainloop()
