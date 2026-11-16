from turtle import Turtle, Screen
class Paddle :
    def __init__(self):
        self.paddles=[]
        self.create_paddles()
    def create_paddles(self):
        positions=((350,0),(-350,0))
        for i in range(2):
            paddle=Turtle()
            paddle.shape("square")
            paddle.shapesize(stretch_wid=5, stretch_len=1)
            paddle.color("white")
            paddle.speed(100)
            paddle.penup()
            paddle.goto(positions[i])
            self.paddles.append(paddle)
    def go_up(self):
        new_y=self.paddles[0].ycor()+20
        self.paddles[0].goto(self.paddles[0].xcor(),new_y)
    def go_down(self):
        new_y = self.paddles[0].ycor() - 20
        self.paddles[0].goto(self.paddles[0].xcor(), new_y)
    def go_up2(self):
        new_y = self.paddles[1].ycor() + 20
        self.paddles[1].goto(self.paddles[1].xcor(), new_y)
    def go_down2(self):
        new_y = self.paddles[1].ycor() - 20
        self.paddles[1].goto(self.paddles[1].xcor(), new_y)

