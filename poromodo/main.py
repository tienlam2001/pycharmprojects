import tkinter as tk
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0
SECOND_MIN = 15
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
SECOND_TIMER = 0

timerStated = True

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

print(time.time())
imageW = 100
imageH = 182
window= tk.Tk()
window.title("Pomodoro")
window.config(padx=100, height=400, bg = YELLOW)
canvas = tk.Canvas(width=200,height=400,bg=YELLOW,highlightthickness=0)
tomato = tk.PhotoImage(file="tomato.png")
canvas.create_image(imageW,imageH, image=tomato)
text_Time = canvas.create_text(103,200,text="25:00", fill = "white", font=(FONT_NAME,35,"bold"))
canvas.pack()
label = tk.Label(text="Timer", font=(FONT_NAME,35,"bold"), bg=GREEN)
label.place(x=40,y=10)

def countFun(minute,second,shortB):
    minuteString =""
    secondString =""
    if not timerStated:
        return False
    if minute == 0 and second == 0:
        minute = shortB

    minuteString = str(minute)
    secondString =str(second)

    if minute < 10:
        minuteString = "0"+str(minute)
    if second < 10:
        secondString = "0"+str(second)

    canvas.itemconfig(text_Time, text=minuteString + ":" + secondString)




    if second == 0:
        minute -= 1
    if minute > 0 and second == 0:
        second = 60
    if second > 0:
        second -= 1




    window.after(1000, countFun, minute, second,shortB)


def startButton(minute,second,shortB):
    global timerStated
    timerStated = True
    countFun(minute,second,shortB)


startB = tk.Button(text="Start", command=lambda:startButton(WORK_MIN,SECOND_MIN,SHORT_BREAK_MIN))
startB.place(x=imageW / 2, y= imageH * 2)

def resetButton(minute,second):
    global timerStated
    timerStated = False
    canvas.itemconfig(text_Time, text="25:00")




resetB = tk.Button(text="Reset", command= lambda:resetButton(WORK_MIN,SECOND_MIN))
resetB.place(x=imageW*2,y=imageH*2)






window.mainloop()