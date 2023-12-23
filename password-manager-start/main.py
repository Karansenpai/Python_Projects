# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import pyperclip

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list=password_numbers+password_symbols+password_letters
    random.shuffle(password_list)

    password_2="".join(password_list)
    Password.insert(0,password_2)
    pyperclip.copy(password_2)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_1=website_input.get()
    email_1=user_input.get()
    pass_1= Password_input.get()

    # messagebox.showinfo(title="Title", message="Message")

    if len(website_1)==0 or len(pass_1)==0:
        messagebox.showinfo(title="Oops", message="please make sure  you haven't left any fields empty")
    else:
        is_ok=messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email_1}" f"\nPassword: {pass_1} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_1} | {email_1} | {pass_1}\n ")
                website_input.delete(0,END)
                Password_input.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Maanager")
window.config(padx=20, pady=20)

canvas=Canvas(width=200, height=200)
image=PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website=Label(text="Website")
website.grid(row=1, column=0)
website.focus()

website_input=Entry(width=35)
website_input.grid(row=1,column=1,columnspan=2)


user=Label(text="Email/Username")
user.grid(row=2,column=0)

user_input=Entry(width=35)
user_input.grid(row=2,column=1,columnspan=2)
user_input.insert(0,'k@gmail.com')

Password=Label(text="Password")
Password.grid(row=3,column=0)

Password_input=Entry(width=21)
Password_input.grid(row=3,column=1)

Generate_Pass=Button(text="Generate Password", command=generate_password)
Generate_Pass.grid(row=3,column=2)

Add=Button(text="Add",width=36,command=save)
Add.grid(row=4,column=1,columnspan=2)

window.mainloop()

