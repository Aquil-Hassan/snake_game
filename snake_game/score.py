from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')
with open("data.txt", mode='r') as file:
    contents=file.read()

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-20, 260)
        self.scores = 0
        self.high_score=int(contents)
        self.update_scoreboard()

    # def game_over(self):
    #     super().clear()
    #     self.goto(0, 0)
    #     super().write(f"Game Over", False, 'center', FONT)
    #     self.goto(-20, 260)
    #     super().write(f"Your final Score: {self.scores}", False, ALIGNMENT, FONT)
    #     self.scores = 0
    # in place of game over method we can use new method called reset method
    def reset(self):
        if self.scores>self.high_score:
            self.high_score=self.scores
            with open('data.txt',mode='w') as file:
                file.write(str(self.high_score))
        self.scores=0
        self.update_scoreboard()

    def update_scoreboard(self):
        super().clear()
        super().write(f"Score: {self.scores} High_Score : {self.high_score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.scores += 1
        self.update_scoreboard()
