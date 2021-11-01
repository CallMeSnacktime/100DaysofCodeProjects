# Import shuffle, choice and randint methods to use them directly
from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = []

    # Randomly select characters in list comprehensions
    pass_letters= [choice(letters) for _ in range(randint(8, 10))]
    pass_symbols= [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers= [choice(numbers) for _ in range(randint(2, 4))]

    #Combine characters and shuffle them
    password_list = pass_letters + pass_symbols + pass_numbers
    shuffle(password_list)
    password = "".join(password_list)

    # Alter password field on UI
    pass_text.delete(0, END)
    pass_text.insert(END, f"{password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = site_text.get()
    user = user_text.get()
    password = pass_text.get()
    if len(site)==0 or len(user) ==0 or len(password)==0:
        messagebox.showinfo(title="Blank Field", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=site, message=f"These are the details entered:\n Website: {site}\n Email: {user}\n Password: {password}\n It it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{site} | {user} | {password}\n")
            pass_text.delete(0, END)
            site_text.delete(0, END)
            messagebox.showinfo(title="Success!!", message="Your credentials were successfully saved!")
# ---------------------------- UI SETUP ------------------------------- #

# Create new window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1, row=0)

# Labels
site_label = Label(text="Website:")
site_label.grid(column=0, row=1)
user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# Entries
site_text = Entry(width=38)
site_text.focus()
site_text.grid(column=1, row=1, columnspan=2)
user_text = Entry(width=38)
user_text.insert(END, "fake@email.com")
user_text.grid(column=1, row=2, columnspan=2)
pass_text = Entry(width=21)
pass_text.grid(column=1, row=3)

# Buttons
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)
gen_button = Button(text="Generate", command=password)
gen_button.grid(column=2, row=3,)


window.mainloop()