import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
move_speed = 0.1
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.turtle_move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(move_speed)
    screen.update()

    car_manager.create_car()
    car_manager.car_moving()

    if player.ycor() == 280:
        player.level_up()
        move_speed *= 0.85
        scoreboard.level_uping()

    for car in car_manager.all_car:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
