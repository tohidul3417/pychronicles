import turtle
import time
import random

# Constants
WIDTH, HEIGHT = 700, 600
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_number_of_racers():
    """Gets the number of racers from the user within the valid range (2-10)."""
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
        print("Invalid input. Please enter a number between 2 and 10.")

def create_turtles(colors):
    """Creates turtle racers and positions them at the starting line."""
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacing_x, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

def draw_finish_line():
    """Draws a finish line at the top of the screen."""
    line = turtle.Turtle()
    line.speed(0)
    line.penup()
    line.setpos(-WIDTH//2, HEIGHT//2 - 10)
    line.pendown()
    line.width(3)
    line.forward(WIDTH)
    line.hideturtle()

def countdown():
    """Displays a countdown before the race starts."""
    count_turtle = turtle.Turtle()
    count_turtle.hideturtle()
    count_turtle.penup()
    count_turtle.color("red")
    
    for i in range(3, 0, -1):
        count_turtle.clear()
        count_turtle.goto(0, 0)
        count_turtle.write(str(i), align="center", font=("Arial", 30, "bold"))
        time.sleep(1)

    count_turtle.clear()
    count_turtle.write("Go!", align="center", font=("Arial", 30, "bold"))
    time.sleep(0.5)
    count_turtle.clear()

def race(turtles):
    """Runs the race and returns the winning turtle's color."""
    while True:
        for racer in turtles:
            distance = random.randint(1, 10)  # Adjusted for smoother movement
            racer.forward(distance)

            # Check if a turtle has reached the finish line
            if racer.ycor() >= HEIGHT // 2 - 20:
                return racer.color()[0]

def init_screen():
    """Initializes the turtle screen."""
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")
    screen.bgcolor("lightgray")

# Main game logic
def main():
    init_screen()
    racers = get_number_of_racers()

    random.shuffle(COLORS)
    colors = COLORS[:racers]

    draw_finish_line()
    turtles = create_turtles(colors)

    countdown()

    winner = race(turtles)
    print("The winner is the turtle with color:", winner)

    # Keep the window open for a few seconds before closing
    time.sleep(5)

if __name__ == "__main__":
    main()
