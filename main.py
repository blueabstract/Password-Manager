import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol= [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers= [random.choice(numbers) for _ in range(nr_numbers)]

    password_list=password_letter+password_symbol+password_numbers

    random.shuffle(password_list)

    passwords="".join(password_list)

    password_entry.insert(0,passwords)

    pyperclip.copy(passwords)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    new_data={
        website: {
            "email": username,
            "password" : password,
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Ooops",message="Please make sure none of the field is left empty!")
    else:

        is_ok= messagebox.askyesno(title=website,message=f"These are the details entered:\n"
                                                         f"Email/Username: {username}\n"
                                                         f"Password: {password}\n"
                                                         f"Is it ok to save?")
        if is_ok:
            try:
                with open("data.json","r") as my_file:
                    #reading the data
                    data = json.load(my_file)
            except FileNotFoundError:
                with open("data.json", "w") as my_file:
                    json.dump(new_data, my_file, indent=4)
            else:
                #updating old data
                data.update(new_data)

                with open("data.json","w") as my_file:
                    json.dump(data,my_file,indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)

def find_password():
    website = website_entry.get()

    try:
        with open("data.json", "r") as my_file:
            # reading the data
            data = json.load(my_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="File Not Found")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email/Username : {email}\n"
                                                      f"Password : {password}")
        else:
            messagebox.showinfo(title=website, message=f"No details for {website} exists")



# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)


canvas=Canvas(height=200,width=200)
my_img=PhotoImage(file="logo.png") #making an image object for canvas.create_image
canvas.create_image(100,100,image=my_img)
canvas.grid(column=1,row=0)

#labels

website_label=Label(text="Website:")
website_label.grid(column=0,row=1)
username_label=Label(text="Email/Username:")
username_label.grid(column=0,row=2)
password_label=Label(text="Password:")
password_label.grid(column=0,row=3)


#Entries

website_entry=Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2,sticky="EW")
website_entry.focus()

username_entry=Entry(width=35)
username_entry.grid(column=1,row=2,columnspan=2,sticky="EW")
username_entry.insert(0,"subarnoshome@gmail.com")

password_entry=Entry(width=21)
password_entry.grid(column=1,row=3,sticky="EW")


#Buttons
generate=Button(text="Generate Password",command=generate_password)
generate.grid(column=2,row=3)

add=Button(text="Add",width=36,command=save)
add.grid(column=1,row=4,columnspan=2,sticky="EW",pady=5)

search_button=Button(text="Search",command=find_password)
search_button.grid(column=2,row=1,columnspan=2,sticky="EW")











window.mainloop()