from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()



    def refresh(self):
        rand_x = random.randint(-270, 270)
        rand_y = random.randint(-270, 270)
        self.goto(rand_x, rand_y)
