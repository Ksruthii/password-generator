import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generatepass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letters=[random.choice(letters) for _ in range(nr_letters)]
    symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    numbers=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list=letters+symbols+numbers
    random.shuffle(password_list)

    password ="".join(password_list)
    entry3.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    entry10=entry1.get()
    entry20 = entry2.get()
    entry30 = entry3.get()
    new_data={
        entry10:{
            "email":entry20,
            "password":entry30,
        }
    }
    if entry10=="" or entry20=="" or entry30=="":
        messagebox.showerror(title="oops",message="don't leave any fields empty")
    else:
        ok=messagebox.askokcancel(title=entry10,message=f"entered details are: \nwebsite:{entry10}\nemial:{entry20}\npassword:{entry30}")
        if ok:
            try:
                with open("output.json","r") as f:
                    data=json.load(f)
            except:
                with open("output.json","w") as f:
                    json.dump(new_data,f,indent=4)
            else:
                data.update(new_data)

                with open("output.json ","w") as f:
                    json.dump(data,f,indent=4)
            finally:
                entry1.delete(0,END)
                entry3.delete(0,END)

# ---------------------------- UI SETUP ---------------------------#
def find_password():
    entry10=entry1.get()
    try:
        with open ("output.json","r") as f:
            data=json.load(f)
    except FileNotFoundError:
        messagebox.showerror(title="error", message="enter the valid name")
    else:
        if entry10 in data:
            entry20=data[entry10]["email"]
            entry30=data[entry10]["password"]
            messagebox.showinfo(title="password", message=f"email:{entry20}\npassword={entry30}")
                    #print(entry1["password"])
        else:
            messagebox.showerror(title="error", message="no details exists")

window=Tk()
window.title("password manager")
window.config(padx=20,pady=20)
canvas=Canvas(width=200,height=200)
photo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=photo)
canvas.grid(column=1,row=0)
label=Label(text="Website:")
label.grid(row=1,column=0)
label=Label(text="Email/Username:")
label.grid(row=2,column=0)
label=Label(text="Password:")
label.grid(row=3,column=0)
entry1=Entry(width=31)
entry1.grid(row=1,column=1,columnspan=2)
entry1.delete(0,'end')
entry2=Entry(width=35)
entry2.grid(row=2,column=1,columnspan=2)
entry3=Entry(width=21)
entry3.grid(row=3,column=1)
button1=Button(text="Generate password",width=14,command=generatepass)
button1.grid(row=3,column=2)
button2=Button(text="add",width=36,command=save)
button2.grid(row=4,column=1,columnspan=2)
button3=Button(text="search",command=find_password)
button3.grid(row=1,column=2)
window.mainloop()