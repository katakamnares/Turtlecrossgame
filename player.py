STARTING_POSITION=(0,-280)
MOVE_DISTANCE=10
FINISH_LINE_R=280
from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
    def move_forward(self):
        self.forward(MOVE_DISTANCE)

