from turtle import Turtle

PADDLE_HEIGHT = 5.0
PADDLE_WIDTH = 1.0


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=PADDLE_WIDTH, stretch_wid=PADDLE_HEIGHT)
        self.color("white")
        self.setposition(position)

    def move_down(self):
        y_position = self.ycor()
        self.sety(y_position - 20)

    def move_up(self):
        y_position = self.ycor()
        self.sety(y_position + 20)


