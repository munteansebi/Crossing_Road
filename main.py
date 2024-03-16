import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.cars()
    car_manager.move_cars()
    for cars in car_manager.all_cars:
        if player.distance(cars) < 25:
            game_is_on = False
            scoreboard.game_over()
    if player.finish():
        player.reset()
        car_manager.increase_speed()
        scoreboard.clear()
        scoreboard.increase_level()

screen.exitonclick()