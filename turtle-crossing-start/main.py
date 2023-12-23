import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.onkey(key="w",fun=player.up)
screen.tracer(0)

game_is_on = Truewqs    `
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #detect collision

    for car in car_manager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()

    #detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()



