from tkinter import *

window = Tk()

window.title("Mile to Km Converter")
window.minsize(width=500,height=300)

mileLabel = Label(text="mile")
mileLabel.place(x=320,y = 0)
mileinput = Entry(width=20)
mileinput.pack()

kmLabel = Label(text="km")
kmLabel.place(x=320,y=30)

kminput = Label(text="")
kminput.place(x=188,y=30)
def convert():
    number = int(mileinput.get())*1.60934
    kminput.config(text=round(number,2))

button= Button(text="Convert",command=convert)
button.place(x=188,y = 50)
window.mainloop()