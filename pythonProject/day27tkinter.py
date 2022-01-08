from tkinter import *

window = Tk()

window.title("My First Gui Program")
window.minsize(width=500,height=300)
#Label
my_lable= Label(text="I am a label")
my_lable.pack()

#Input
input = Entry(width=10)
input.pack()
def button_clicked():


#Button
button = Button(text="Click me", command= button_clicked)
button.pack()


# Must be the end of the program
window.mainloop()