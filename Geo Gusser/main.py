import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_name = data.state.to_list()


gussed_state = []

while len(gussed_state) < 50 :

    answer = screen.textinput(title=f"{len(gussed_state)}/50. Guess the State",
                              prompt="What's the another State Name??").title()

    if answer == "Exit":
        missed_state = []
        for state in state_name:
            if state not in gussed_state:
                missed_state.append(state)
        new_data = pandas.DataFrame(missed_state)
        new_data.to_csv("States To Learn.csv")
        break

    if answer in state_name:
        gussed_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer)

