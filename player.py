from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.setheading(270)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")


    def up(self):
        if self.ycor() < 240:
            self.forward(-30)
    def down(self):
        if self.ycor() > -240:
            self.forward(30)
