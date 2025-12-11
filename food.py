import turtle
from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.shape("circle")
        self.penup()
        self.color('blue')
        turtle.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.score += 1