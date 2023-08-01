from turtle import Turtle, Screen
from player import Player
from ball import Ball
import time
from scoreboard import Board



screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.tracer(2)

p1 = Player()
p1.goto(x=350, y=0)
p2 = Player()
p2.goto(x=-350, y=0)

bal = Ball()
board = Board()


screen.listen()
screen.onkeypress(key="Up", fun=p1.up)
screen.onkeypress(key="Down",fun=p1.down)
screen.onkeypress(key="w", fun=p2.up)
screen.onkeypress(key="s", fun=p2.down)

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()
    bal.check()
    bal.move()
    if bal.xcor() > 320:
        if p1.distance(bal) < 50:
            bal.collision_p1()
            print("made contact")
        else:
            board.score(2)
            bal.goto(0,0)


    elif bal.xcor() < -340:
        if p2.distance(bal) < 50:
            bal.collision_p2()
            print("made contact")
        else:
            board.score(1)
            bal.goto(0,0)






























screen.exitonclick()






