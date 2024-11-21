from turtle import Turtle
import random


class Snake:
    """Represents the snake in the game."""

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the initial snake body."""
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_positions:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a new segment to the snake."""
        segment = Turtle("square")
        segment.color(self.random_color())
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        """Extends the snake by adding a new segment at the tail."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves the snake forward by shifting all segments."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def random_color(self):
        """Generates a random color for the snake segments."""
        return random.choice(["red", "blue", "green", "yellow", "purple", "orange"])

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
