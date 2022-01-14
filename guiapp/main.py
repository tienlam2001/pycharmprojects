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


window = tk.Tk()
window.title("Gui App")

window.config(padx=100,width=400,height=800,bg=BACKGROUND_COLOR)
canvas = tk.Canvas(width=400,height=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0)


window.mainloop()