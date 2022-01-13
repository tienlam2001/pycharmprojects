import tkinter as tk
import csv
import pandas
from random import randrange
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"

#UI Setup
YELLOW = "#f7f5dd"
window = tk.Tk() # Create mainframe
window.title("Flashcard")
frame = tk.Frame(window,bg=YELLOW,width= 500,height=200)
frame.grid(row=1,column=0)

# Variable

try:
    data = pandas.read_csv("./data/words_to_learn.csv") #data restored all the french and english words
except FileNotFoundError:
    data= pandas.read_csv("./data/french_words.csv")


to_learn = data.to_dict(orient="records") #Change data to dictionary as record
print(len(to_learn))
isFront = True # checking if the card is facing front
randomN = randrange(0,len(to_learn))


window.config(padx=100,width=1200, height=900,bg=BACKGROUND_COLOR)

canvas = tk.Canvas(width=1000, height= 600, bg =BACKGROUND_COLOR,highlightthickness=0)
cardback = tk.PhotoImage(file="./images/card_back.png")
cardfront = tk.PhotoImage(file="./images/card_front.png")
image_canvas= canvas.create_image(500,300,image=cardfront,anchor="center")
textLanguage = canvas.create_text(500,100,text="French", font=(FONT_NAME,30))
text_canvas=canvas.create_text(500,300,text=to_learn[randomN]["French"], font=(FONT_NAME,50))
canvas.grid(row=0, column=0)


#Functions wrong and right


def autoFlipCard():     # This is function to flip the cards
    global to_learn     #Global data retored in data
    global randomN      #GLobal randomNumber

    global isFront
    print("Timer is running")
    if isFront:                                     # If the front the card will be fliped
        canvas.itemconfig(textLanguage,text="English")       # Set the title of the card to be English
        canvas.itemconfig(image_canvas,image=cardback)       # Set the image to cardback
        canvas.itemconfig(text_canvas,text=to_learn[randomN]["English"])    # Set the text to be english words
        isFront=False


def runningTimer():                         # Set up the running timer
    global timer                            # Timer To Control
    global isFront
    print("Runing Timer is Running")
    if isFront:                             # If the card is facing front
        timer = window.after(3000,autoFlipCard)     # We will flip the cards
    elif not isFront:
        print("Timer stoped")

timer = window.after(3000, runningTimer)    # Timer Will Automate after 3s


def nextQuestion():                     # When the user click right button
    global timer
    global isFront          # Making sure that the card is facing front
    isFront = True          # Set it to be true
    global to_learn
    global randomN
    to_learn.pop(randomN)                   # pop the index out of the list
    window.after_cancel(timer)              # Let cancel all the timer
    dataConvert = pandas.DataFrame(to_learn)    # Convert to data dataframe
    dataConvert.to_csv("./data/words_to_learn.csv") # Convert data to csv type
    randomN = randrange(0, len(to_learn))

    canvas.itemconfig(textLanguage,text="French")
    canvas.itemconfig(image_canvas, image=cardfront)        # Set image to front
    canvas.itemconfig(text_canvas, text=to_learn[randomN]["French"])    # Set text to french
    runningTimer()




# Next question always the front and time to flip to the back



wrong = tk.PhotoImage(file="./images/wrong.png")
wrongButton = tk.Button(frame,text="Wrong",image=wrong,width=150,bg=BACKGROUND_COLOR,highlightthickness=0)
wrongButton.grid(row=0,column=0)
right = tk.PhotoImage(file="./images/right.png")
rightButton = tk.Button(frame,image=right,text="Didn't Remember",width=150,bg=BACKGROUND_COLOR,highlightthickness=0,command=nextQuestion)
rightButton.grid(row=0,column=1)

window.mainloop()


