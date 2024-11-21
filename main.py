from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def setup_screen():
    """Initializes and sets up the game screen."""
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    draw_border()
    return screen


def draw_border():
    """Draws a border around the game area."""
    border = Turtle()
    border.color("white")
    border.penup()
    border.goto(-290, -290)
    border.pendown()
    border.pensize(3)
    for _ in range(4):
        border.forward(580)
        border.left(90)
    border.hideturtle()


def main():
    # Screen setup
    screen = setup_screen()

    # Game objects
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    # Controls
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    # Main game loop
    game_is_on = True
    speed = 0.2
    while game_is_on:
        screen.update()
        time.sleep(speed)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            scoreboard.increase_score()
            snake.extend()
            speed *= 0.95  # Increase speed as the game progresses

        # Detect collision with wall
        if (
            snake.head.xcor() > 280
            or snake.head.xcor() < -280
            or snake.head.ycor() > 280
            or snake.head.ycor() < -280
        ):
            game_is_on = False
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    main()
