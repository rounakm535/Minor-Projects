from turtle import Screen, Turtle
from pad import Pad
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Developed by Rounak Mishra")
screen.tracer(0)

r_pad = Pad((350, 0))
l_pad = Pad((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_pad.go_up, "Up")
screen.onkeypress(r_pad.go_down, "Down")
screen.onkeypress(l_pad.go_up, "w")
screen.onkeypress(l_pad.go_down, "s")

game_on = True

while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_pad) < 50 and ball.xcor() > 320 or ball.distance(l_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()

screen.exitonclick()
