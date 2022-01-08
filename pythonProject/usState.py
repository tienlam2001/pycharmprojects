import turtle
import pandas

data = pandas.read_csv("50_states.csv")
stateList = data["state"].to_list()
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
drawer = turtle.Turtle()
turtle.shape(image)
drawer.hideturtle()
drawer.penup()
#
# drawer.write("First Last",align="right")
while True:
    answer_state = screen.textinput(title="Guess the State", prompt="What state name")
    answer_state=answer_state.capitalize()
    if answer_state in stateList:
        index = stateList.index(answer_state)
        newData = data[data.state==answer_state].to_dict()
        drawer.setposition(newData['x'][index],newData['y'][index])
        drawer.write(answer_state,align="right")
    else:
        print("none")

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()