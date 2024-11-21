from turtle import Turtle


class Scoreboard(Turtle):
    """Displays the score and game over message."""

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_score()

    def update_score(self):
        """Updates the scoreboard with the current score."""
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        """Increases the score and updates the scoreboard."""
        self.score += 1
        self.update_score()

    def game_over(self):
        """Displays the game over message."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 36, "bold"))
