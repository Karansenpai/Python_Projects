from turtle import Turtle,Screen
import random

class Paddle(Turtle):
    def __init__(self,ori="left"):
        super().__init__()
        self.create_paddle(ori)

    def create_paddle(self,ori):
        if ori == "left":
                self.shape("square")
                self.color("yellow")
                self.shapesize(stretch_wid=5, stretch_len=1)
                self.penup()
                self.goto(-350,0)

        else:
                self.shape("square")
                self.color("yellow")
                self.shapesize(stretch_wid=5, stretch_len=1)
                self.penup()
                self.goto(350,0)


    def up(self):
        if self.ycor()>220:
            pass
        else:
            new_y=self.ycor()+40
            self.goto(self.xcor(),new_y)

    def down(self):
        if self.ycor()<-220:
            pass
        else:
            new_y = self.ycor() - 40
            self.goto(self.xcor(), new_y)





