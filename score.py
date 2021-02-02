from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.hideturtle()
        self.current_score = 0
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.current_score}", align="center", font=("Courier", 14, "bold"))

    def add_score(self):
        self.clear()
        self.current_score += 1
        self.update_score()

    def end_game(self):
        self.goto(0, 0)
        self.write(f"G4M3 0V3R", align="center", font=("Courier", 14, "bold"))
