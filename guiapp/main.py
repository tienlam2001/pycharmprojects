import tkinter as tk
import random
import json
import html
import requests
BACKGROUND_COLOR = "#B1DDC6"
# dataLink = "https://opentdb.com/api.php"
# parameter = {
#     "amount": 10
# }
#
# data = requests.get(dataLink, params=parameter)
# dataRestore = data.json()
#
# for i in range(10):
#     print(html.unescape(dataRestore["results"][i]["question"]))

YELLOW = "#f7f5dd"
window = tk.Tk()
window.title("Gui App")
frame = tk.Frame(window,bg =BACKGROUND_COLOR, width= 200,height=200)      # Create Frame
window.config(padx=100,width=400,height=600)
canvas = tk.Canvas(window,width=400,height=600, bg=YELLOW, highlightthickness=0) # Create Canvas that will contain text
canvas.grid(row=0,column=0)             # Place the canvas at the position
frame.grid(column=0,row=1)              # Place the container of Buttons at the position
wrongButtonI = tk.PhotoImage(file="images/false.png") # Create picture for wrong button
rightButtonI = tk.PhotoImage(file="images/true.png") # Create picture for right button

falseButton = tk.Button(frame)          # Create False Button

window.mainloop()