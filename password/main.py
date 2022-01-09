import tkinter as tk
from tkinter import messagebox
from random import randrange
import string
import json

imageW = 100
imageH = 182

class Password:
    def __init__(self,website,user,password):
        self.website = website
        self.user = user
        self.password = password

    def printDic(self):
        return{websiteName: self.website, username: self.user, pas: self.password}

FONT_NAME = "Courier"
YELLOW = "#f7f5dd"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generateButton():
    global inputPassword
    randomLength = randrange(8,33)
    passwordUser = ""
    for i in range(randomLength):
        passw = string.printable[randrange(len(string.printable))]

        if len(passwordUser) > 2:
            while passwordUser[len(passwordUser) - 1] == passw and passwordUser[len(passwordUser) - 2] ==passw:
                passw = string.printable[randrange(len(string.printable))]

        passwordUser += passw

    inputPassword.delete(0,"end")
    inputPassword.insert(0,passwordUser)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def addPass(website,username,password):

    if website.get() =="" or username.get() =="" or password.get() =="":
        messagebox.showinfo(title="Error !", message="can't leave boxes empty")
        return None

    restoreWebsite = website.get()
    restoreUsername = username.get()
    restorePassword = password.get()
    newData = {
        restoreWebsite: {
        "username": restoreUsername,
        "password": restorePassword
        }
    }

    isOk = tk.messagebox.askokcancel(title=website,message=f"Do you want to save \n {website.get()}, \n {username.get()}, \n {password.get()}")
    if isOk:
        dataJson = open("data.json", "r")           # Read true data
        data = json.load(dataJson)                  # restore the true data
        data.update(newData)                        # Add new Data

        dataJson = open("data.json", "w")           # Able to write on true data
        json.dump(data, dataJson,indent=2)          # Add the whole thing in to true data
        data = open("de.txt", "r")
        if len(data.readlines()) == 0:
            data = open("de.txt", "a")
            data.write(website.get()+ "|"+username.get()+"|"+password.get())
            inputWebsite.delete(0,"end")
            inputPassword.delete(0,"end")
            data.close()
        else:
            data = open("de.txt", "a")
            data.write("\n")
            data.write(website.get() + "|" + username.get() + "|" + password.get())
            inputWebsite.delete(0, "end")
            inputPassword.delete(0, "end")
            data.close()


def searchPassword(website):
    datajson = open('data.json', 'r')
    data = json.load(datajson)
    try:
        print(data[website.get()])
    except KeyError:
        print("can't Find the account")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx = 100,width=500, height=400)
canvas = tk.Canvas(width=200,bg=YELLOW,highlightthickness=0)
tomato = tk.PhotoImage(file="logo.png")
canvas.create_image(imageW,imageH, image=tomato)
canvas.grid(row=0,column=1)

#Website of Password
websiteName = tk.Label(text="Website", font=(FONT_NAME,10))
websiteName.grid(column=0,row=2)
inputWebsite = tk.Entry(window,width=50)
inputWebsite.grid(column=1,row=2)
searchButton = tk.Button(text="Search", command= lambda:searchPassword(inputWebsite),width=20)
searchButton.grid(column=2,row=2)

#Email/user
username = tk.Label(text="Email/User", font=(FONT_NAME,10))
username.grid(column=0,row=3)
inputuser = tk.Entry(window,width=75)
inputuser.grid(column=1,row=3,columnspan=2)

#Password
password = tk.Label(text="Password", font=(FONT_NAME,10))
password.grid(column=0,row=4)
inputPassword = tk.Entry(window,width=50)
inputPassword.grid(column=1,row=4)
# inputPassword.insert(0)
generatePassword = tk.Button(text="Generate Password",command=generateButton)
generatePassword.grid(column=2,row=4)

#Add Button
addButton = tk.Button(text="Add",width=35,command=lambda:addPass(inputWebsite,inputuser,inputPassword))
addButton.grid(row=5,column=1)

#Main Loop
window.mainloop()