from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, username, high_score=0):
        super().__init__()
        self.username = username
        self.score = 0
        self.high_score = high_score
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.username} | Score: {self.score} | High Score: {self.high_score}", align="center", font=("Courier", 14, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def increase_bonus_score(self):
        self.score +=2
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "bold"))

    def get_score(self):
        return self.score
