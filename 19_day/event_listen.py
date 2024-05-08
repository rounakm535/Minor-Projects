from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def a_cwise():
    tim.right(10)


def cwise():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.listen()
screen.onkey(key="w" , fun=forward)
screen.onkey(key="s", fun= backward)
screen.onkey(key="a", fun= a_cwise)
screen.onkey(key="d", fun= cwise)
screen.onkey(key="c", fun= clear)



screen.exitonclick()