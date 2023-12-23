from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.tim = Turtle()
        self.tim.color("white")
        self.tim.pensize(3)
        self.tim.width(5)
        self.tim.penup()
        self.tim.goto(0, -250)
        self.tim.setheading(90)
        self.move()

    def move(self):
        for i in range(50):
            self.tim.pendown()
            self.tim.forward(5)
            self.tim.penup()
            self.tim.forward(10)
