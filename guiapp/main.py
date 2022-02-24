import tkinter as tk
import random
import json
import html
import requests
BACKGROUND_COLOR = "#B1DDC6"
dataLink = "https://opentdb.com/api.php"
parameter = {
    "amount": 10
}

data = requests.get(dataLink, params=parameter)
dataRestore = data.json()
FONT_NAME = "Courier"
score = 0
for i in range(10):
    print(html.unescape(dataRestore["results"][i]["question"]))

YELLOW = "#f7f5dd"
window = tk.Tk()
window.title("Gui App")
frame = tk.Frame(window,bg =BACKGROUND_COLOR, width= 200,height=200)      # Create Frame
window.config(padx=100,width=400,height=600)

canvas = tk.Canvas(window,width=400,height=600, bg=YELLOW, highlightthickness=0) # Create Canvas that will contain text
text = tk.Text(canvas)
text.insert(tk.END,html.unescape(dataRestore["results"][1]["question"]))
text.pack()
# canvasText = canvas.create_text(200,300,text=html.unescape(dataRestore["results"][1]["question"]),font=(FONT_NAME,20))
canvas.grid(row=0,column=0)             # Place the canvas at the position
frame.grid(column=0,row=1)              # Place the container of Buttons at the position

def wrongButtonFuc():
    return 0

def rightButtonFunc():
    return 0

wrongButtonI = tk.PhotoImage(file="images/false.png") # Create picture for wrong button
rightButtonI = tk.PhotoImage(file="images/true.png") # Create picture for right button

falseButton = tk.Button(frame, command= wrongButtonFuc,image=wrongButtonI, width = 150)          # Create False Button
falseButton.pack(side=tk.LEFT)
rightButton = tk.Button(frame, command= rightButtonFunc, image=rightButtonI, width = 150)
rightButton.pack(side=tk.RIGHT)
window.mainloop()