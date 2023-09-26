from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title= "Oops", message="Please fill in all fields!")


    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            password_entry.delete(0, END)
            website_input.delete(0, END)

def find_password():
    website = website_input.get().capitalize()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="Credentials", message=f"Email: {email}Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")




# ---------------------------- UI SETUP ---------------------------- --- #

window = Tk()
window.title("Password Manager")

window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100 , image = lock_img)
canvas.grid(column=1, row =0)

#Website label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

#Website input
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()

#Email/Username label
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

#Email/Username input
username_entry= Entry(width=40)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "andrei5dulama@yahoo.com")


#Password label
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

#Add Button
add_button = Button(text="Add", width=38, command=save)
add_button.grid(column=1, row=4, columnspan=2)

#Generate password button
gen_pass = Button(text="Generate Password", width=15, command=generate_password)
gen_pass.grid(column=2, row=3)

#Password input/generate
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

#Search button
search = Button(text="Search", width=15, command=find_password)
search.grid(column=2, row=1)


window.mainloop()
