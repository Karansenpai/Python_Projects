from turtle import Screen
from middle_line import Line
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


# row line in middle
line = Line()
screen.update()

#paddle
paddle_left = Paddle("left")
paddle_right = Paddle("right")

#paddle movements
screen.listen()



screen.onkey(key="w",fun=paddle_left.up)
screen.onkey(key="s",fun=paddle_left.down)

screen.onkey(key="Up",fun=paddle_right.up)
screen.onkey(key="Down",fun=paddle_right.down)




#ball

ball=Ball()


game_is_on=True


def exit():
   global game_is_on
   game_is_on=False
   ball.write("game ended", align="center", font=("Courier", 50, "normal"))


screen.onkey(key="Escape",fun=exit)


scoreboard=Scoreboard()

while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # collision with walls
    if ball.ycor()>280 or ball.ycor() < -280:
        ball.bounce_y()


    #detect with right paddle
    if ball.distance(paddle_right) <50 and ball.xcor()>320 or ball.distance(paddle_left)<50 and ball.xcor()<-320:
        ball.bounce_x()

    #detect miss
    if ball.xcor()>380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor()<-380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
