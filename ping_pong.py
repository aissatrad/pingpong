from turtle import Turtle, Screen, textinput
from tkinter import messagebox


def create_shape(x, y, stretch_w, stretch_y, shape_name="square"):
    shape = Turtle()
    shape.speed(0)
    shape.shape(shape_name)
    shape.shapesize(stretch_wid=stretch_w, stretch_len=stretch_y)
    shape.color("#ffffff")
    shape.penup()
    shape.goto(x, y)
    return shape


class Player(Turtle):
    score = 0

    def __init__(self, p_name, x, y, color):
        super().__init__()
        self.p_name = p_name
        self.shape("square")
        self.speed(0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(color)
        self.penup()
        self.goto(x, y)

    def inc_score(self):
        self.score += 1

    def up(self):
        if self.ycor() <= 250:
            self.sety(self.ycor() + 30)

    def down(self):
        if self.ycor() >= -250:
            self.sety(self.ycor() - 30)


wind = Screen()
wind.title("Ping Pong")
wind.bgcolor("green")
wind.setup(width=800, height=600)
wind.tracer(0)

game_type = textinput("Choose Game Type:", "Enter:\n[1] player vs pc \n[2] two players")

if game_type == "2":
    p_1_name = textinput("", "Player 1 name")
    p_2_name = textinput("", "Player 2 name")
    player_1 = Player(p_1_name.upper(), -350, 0, "blue")
    player_2 = Player(p_2_name.upper(), 350, 0, "red")
elif game_type == "1":
    p_2_name = textinput("", "Player 2 name")
    player_1 = Player("PC", -350, 0, "blue")
    player_2 = Player(p_2_name.upper(), 350, 0, "red")
else:
    p_2_name = textinput("", "Player 2 name")
    player_1 = Player("PC", -350, 0, "blue")
    player_2 = Player(p_2_name.upper(), 350, 0, "red")

ball = create_shape(0, 0, 1, 1, shape_name="circle")
ball.dx = 0.4
ball.dy = 0.4

line = create_shape(0, 0, 40, 0.2)
center = create_shape(0, 0, 1.5, 1.5, shape_name="circle")
right = create_shape(400, 0, 40, 1)
left = create_shape(-400, 0, 40, 0.4)
top = create_shape(0, 300, 0.4, 40)
bottom = create_shape(0, -300, 1, 40)
score = create_shape(0,260,1,1)
score.hideturtle()
score.write(f"{player_1.p_name} : {player_1.score}\t\t{player_2.p_name} : {player_2.score}",
            align="center", font=("Arial", 24, "bold"))
wind.listen()
wind.onkeypress(player_1.up, "s")
wind.onkeypress(player_1.down, "w")

wind.onkeypress(player_2.up, "Up")
wind.onkeypress(player_2.down, "Down")
wind.cv._rootwindow.resizable(False, False)

player_1.dy = -1
while True:
    try:
        wind.update()

        if game_type == "1":
            player_1.sety(player_1.ycor() + player_1.dy)
            if player_1.ycor() > 250:
                player_1.dy *= -1
            if player_1.ycor() < -250:
                player_1.dy *= -1

        if player_1.score == 10 or player_2.score == 10:
            winner = create_shape(-200, 200, 1, 1)
            winner.color("orange")
            winner.hideturtle()
            w = player_1 if player_1.score > player_2.score else player_2
            winner.write(f"{w.p_name} Win :)", align="center", font=("Arial", 36, "bold"))
            res = messagebox.askokcancel("Play Again", "do you want to play again")

            if not res:
                wind.bye()
            else:
                winner.clear()
                player_1.score = 0
                player_2.score = 0
                score.clear()
                score.write(f"{player_1.p_name} : {player_1.score}\t\t{player_2.p_name} : {player_2.score}",
                            align="center", font=("Arial", 24, "bold"))

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            player_1.inc_score()
            score.clear()
            score.write(f"{player_1.p_name} : {player_1.score}\t\t{player_2.p_name} : {player_2.score}",
                        align="center", font=("Arial", 24, "bold"))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            player_2.inc_score()
            score.clear()
            score.write(f"{player_1.p_name} : {player_1.score}\t\t{player_2.p_name} : {player_2.score}", align="center",
                        font=("Arial", 24, "bold"))

        if 340 < ball.xcor() < 350 and player_2.ycor() + 40 > ball.ycor() > player_2.ycor() - 40:
            ball.setx(340)
            ball.dx *= -1

        if -340 > ball.xcor() > -350 and player_1.ycor() + 40 > ball.ycor() > player_1.ycor() - 40:
            ball.setx(-340)
            ball.dx *= -1
    except:
       exit(0)
