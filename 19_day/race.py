from turtle import Turtle, Screen
import random

race_on = False

screen = Screen()
screen.setup(500, 400)
bet = screen.textinput(title="Make your bet!!", prompt= "Choose your colour: ")
colors = ["red", "green", "orange", "yellow", "blue", "purple"]
y_coord = [-70, -40, -10, 20, 50, 80]
turtles = []


for turtle in range(0, 6):
    new_tur = Turtle(shape="turtle")
    new_tur.color(colors[turtle])
    new_tur.penup()
    new_tur.goto(x = -230, y = y_coord[turtle])
    turtles.append(new_tur)


if bet:
    race_on = True

while race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_on = False
            winner  = turtle.pencolor()
            if winner == bet:
                print(f"Yeah you won!!!! The winner is {winner} ")
            else:
                print(f"You lose :( ! The winner is {winner} ")

        distance = random.randint(0, 10)
        turtle.forward(distance)




screen.exitonclick()