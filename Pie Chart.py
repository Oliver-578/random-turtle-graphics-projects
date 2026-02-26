import turtle as t
import random as r

# setup screen
t.bgcolor("black")
t.screensize(400, 400)

# turtle for drawing the pie chart
pie = t.Turtle()
pie.speed(0)

colors = ["red", "yellow", "green", "blue", "orange", "purple", "cyan", "magenta", "lime"]

# Generate random angles that add up to 360
line = r.randint(10, 20)
angles = [r.randint(1, 100) for _ in range(line)]
total = sum(angles)
angles = [a / total * 360 for a in angles]

current_angle = 0

for angle in angles:
    pie.home()
    pie.left(current_angle)
    pie.color(r.choice(colors))
    pie.fillcolor(r.choice(colors))
    pie.begin_fill()
    pie.forward(200)
    pie.left(90)
    pie.circle(200, angle)
    pie.home()
    pie.end_fill()
    current_angle += angle

# circle outline for the pie chart
pie.color("white")
pie.penup()
pie.goto(0, -200)
pie.pendown()
pie.setheading(0)
pie.circle(200)

t.done()