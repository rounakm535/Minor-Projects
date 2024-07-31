from turtle import Turtle

class Pad(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos)

    def go_up(self):
        update_y = self.ycor() + 30
        self.goto(self.xcor(), update_y)

    def go_down(self):
        update_y = self.ycor() - 30
        self.goto(self.xcor(), update_y)
