import random
from turtle import Turtle
from random import randint
rand = [(randint(210,255)), (randint(285,330))]
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(1)
        self.speed("fastest")
        self.setheading(random.choice(rand))


    def move(self):
        self.forward(25)

    def check(self):
        if self.ycor() > 280 or self.ycor() < -280:
            head = - self.heading()
            self.setheading(head)
    def collision_p2(self):
        head = randint(-80,80)
        self.setheading(head)

    def collision_p1(self):
        head = randint(100,260)
        self.setheading(head)



