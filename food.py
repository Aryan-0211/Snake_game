from turtle import Turtle
import random


class Food(Turtle):
    """Represents the food in the game."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Repositions the food at a random location on the screen."""
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.color(self.random_color())
        self.goto(random_x, random_y)

    def random_color(self):
        """Generates a random color for the food."""
        return random.choice(["red", "blue", "green", "yellow", "purple", "orange"])
