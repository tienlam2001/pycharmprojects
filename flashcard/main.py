import tkinter as tk



#UI Setup

window = tk.Tk() # Create mainframe
window.title("Flashcard")



canvas = tk.Canvas(width=900, height= 900)
cardback = tk.PhotoImage(file="./images/card_back.png")
cardfront = tk.PhotoImage(file="./images/card_front.png")
canvas.create_image(450,300,image=cardfront,anchor="center")
canvas.create_text(450,300,text="this is text")
canvas.grid(row=0, column=0)

window.mainloop()

BACKGROUND_COLOR = "#B1DDC6"

