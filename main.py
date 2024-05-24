import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(key="Up",fun=player.move_forward)
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.car_created()
    car_manager.move()
    for car in car_manager.all_cars:
        if car.distance(player)<20:
            scoreboard.game_over()
            game_is_on=False
        if player.ycor()>280:
            player.goto(0,-280)
            car_manager.reset_position()
            scoreboard.increment_score()


screen.exitonclick()


