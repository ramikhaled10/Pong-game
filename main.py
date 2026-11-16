from Paddles import Paddle
from turtle import Turtle, Screen
import time
from ball import Ball_Paddel
from score_board import Score_Board
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong_game")
screen.tracer(0)
net = Turtle()
net.color("white")
net.hideturtle()
net.penup()
net.goto(0, -300)  # Start from bottom center
net.setheading(90)  # Face upwards

# Draw dashed line up the screen
for _ in range(30):
    net.pendown()
    net.forward(10)
    net.penup()
    net.forward(10)

Paddle = Paddle()
ball=Ball_Paddel()
score_board = Score_Board()
is_game_over = False
time_sleep=0.1
while not is_game_over:
    screen.update()
    time.sleep(time_sleep)
    screen.listen()
    screen.onkeypress(Paddle.go_up, "Up")
    screen.onkeypress(Paddle.go_down, "Down")
    screen.onkeypress(Paddle.go_up2 ,"w")
    screen.onkeypress(Paddle.go_down2, "s")
    ball.ball_move()
    ball.bounce_y()
    if (ball.distance(Paddle.paddles[0])<50 and ball.xcor()>330) or (ball.distance(Paddle.paddles[1])<50 and ball.xcor()<-330):
        time_sleep*=0.9
        ball.bounce_x()
        ball.speed()
    if ball.xcor()>380 :
        ball.reset_postion()
        ball.bounce_x()
        score_board.l_win()
        time_sleep=0.1
    if ball.xcor()<-380 :
        ball.reset_postion()
        ball.bounce_x()
        score_board.r_win()
        time_sleep=0.1























screen.exitonclick()