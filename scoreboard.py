FONT=("courier",24,"normal")
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=1
        self.penup()
        self.hideturtle()
        self.goto(-230,255)
        self.update()
    def update(self):
        self.clear()
        self.write(f"Level:{self.score}",align="left",font=FONT)
    def increment_score(self):
        self.score+=1
        self.update()

    def game_over(self):
        self.home()
        self.write("Game over",align="center",font=FONT)
