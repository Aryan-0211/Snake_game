from turtle import Turtle


class Scoreboard(Turtle):
    """Displays the score and game over message."""

    def __init__(self):
        super().__init__()
        self.score = 0
        
        with open("data.txt") as data:
            self.high_score = int(data.read())
            
            
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.update_score()

    def update_score(self):
        """Updates the scoreboard with the current score."""
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score   
            with open("data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()      

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        
   # def game_over(self):
    #    """Displays the game over message."""
     #   self.goto(0, 0)
      #  self.write("GAME OVER", align="center", font=("Arial", 36, "bold"))
