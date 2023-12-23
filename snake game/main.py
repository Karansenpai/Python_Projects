from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard
import time

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

# creating a body
snake=Snake()
food=Food()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

# moving a snake
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.07)
    snake.move()

    #detect collision with food
    if snake.head.distance(food) <17:
         food.refresh()
         snake.extend()
         scoreboard.increase_score()

    #detect collision with walls
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor() >290 or snake.head.ycor() <-290:
        game_is_on=False
        scoreboard.game_over()

    #detect collision with tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) <10:
            game_is_on=False
            scoreboard.game_over()





screen.exitonclick()



