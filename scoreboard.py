from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        """Clears the screen and writes the current score."""
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align =ALIGNMENT,font = FONT)
    
    def increase_score(self):
        """Increases the score and updates the scoreboard."""
        self.score += 1
        self.update_score()
