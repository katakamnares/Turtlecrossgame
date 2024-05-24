COLORS=["red","orange","yellow","green","blue","purple"]
STARTING_MOVING_DISTANCE=5
MOVE_INCREMENT=10
from turtle import Turtle
import random
class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.move_speed=STARTING_MOVING_DISTANCE
    def car_created(self):
        random_n = random.randint(1,6)
        if random_n==1:
            car=Turtle()
            car.shape("square")
            car.penup()
            car.color(random.choice(COLORS))
            new_y=random.randint(-250,250)
            car.goto(300,new_y)
            self.all_cars.append(car)
    def move(self):
        for cars in self.all_cars:
            cars.backward(self.move_speed)
    def reset_position(self):
        self.move_speed+=MOVE_INCREMENT






