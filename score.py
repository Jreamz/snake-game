from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.current_score = 0
        self.high_score = self.read_score()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", align="center", font=("Courier", 14, "bold"))

    def add_score(self):
        self.current_score += 1
        self.update_score()

    def reset(self):
        if self.current_score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(f"{self.current_score}")
            self.high_score = self.current_score
        self.current_score = 0
        self.update_score()

    def read_score(self):
        with open("data.txt", mode="r") as file:
            return int(file.read())
