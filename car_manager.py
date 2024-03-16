from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []

    def cars(self):
        rand = random.randint(1, 6)
        if rand == 2:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.setheading(0)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE+MOVE_INCREMENT)