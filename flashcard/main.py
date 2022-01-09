import tkinter as tk



#UI Setup

window = tk.Tk() # Create mainframe
window.title("Flashcard")
window.config(width= 800, height= 800)
canvas = tk.Canvas(width=700, height= 400, highlightthickness = 0)
cardfront = tk.PhotoImage(file="./images/card_front.png")
canvas.create_image(700,400,image=cardfront)
canvas.grid(row = 0, column=0)

window.mainloop()

BACKGROUND_COLOR = "#B1DDC6"

