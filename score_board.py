from turtle import Turtle
class Score_Board(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score=0
        self.r_score=0
        self.score_update()
    def score_update(self):
       self.goto(-100, 230)
       self.write(f"{self.l_score} ", align="center", font=("courier", 45, "bold"))
       self.goto(150, 230)
       self.write(f"{self.r_score} ", align="center", font=("courier", 45, "bold"))
    def l_win(self):
        self.l_score+=1
        self.clear()
        self.score_update()
    def r_win(self):
        self.r_score+=1
        self.clear()
        self.score_update()