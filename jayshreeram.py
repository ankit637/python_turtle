# Devotional Python Turtle Artwork - Jai Shree Ram

from turtle import *

def setup_drawing_environment():
    title('Jai Shree Ram')
    bgcolor('black')
    pensize(5)
    pencolor("orange")

def draw_devotional_pattern():
    Ram_naam = ["जय श्री राम"] * 49  # List of "Jai Shree Ram" in Hindi
    angle = 360 / 49  # Angle between each iteration
    penup()
    sety(-1)

    for i in range(49):  # Ensure there are enough elements in the list
        left(angle)
        forward(260)
        write(Ram_naam[i], align="right", font=('Arial', 12, "bold"))
        backward(260)

def add_final_touch():
    penup()
    goto(-40, -20)
    pendown()
    write("|| जय श्री राम ||", font=("Arial", 55, "normal"), align="center")
    hideturtle()

def main():
    setup_drawing_environment()
    draw_devotional_pattern()
    add_final_touch()
    done()

if __name__ == "__main__":
    main()
