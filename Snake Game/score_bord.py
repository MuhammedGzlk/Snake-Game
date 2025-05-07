from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write_score()


    def write_score(self):
        self.clear()
        self.color('blue')
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)