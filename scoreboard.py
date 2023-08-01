from turtle import Turtle

class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1 = 0
        self.p2 = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.p1, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.p2, align="center", font=("Courier", 80, "normal"))


    def score(self,p):
        if p == 2:
            self.p1 +=1
        elif p == 1:
            self.p2 +=1
        self.refresh()



