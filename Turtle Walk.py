import turtle as t
import random as r

screen = t.Screen()
screen.bgcolor("black")

g = t.Turtle()
g.color("white")
g.speed(0)

w = t.Turtle()
w.color("lime green")
w.speed(6)

CELL = 60
SIZE = 8

for i in range(SIZE + 1):
    g.penup()
    g.goto(i * CELL - 240, -240)
    g.pendown()
    g.goto(i * CELL - 240, 240)

for i in range(SIZE + 1):
    g.penup()
    g.goto(-240, i * CELL - 240)
    g.pendown()
    g.goto(240, i * CELL - 240)

w.penup()
w.goto(-240, -240)
w.pendown()

col = 0
row = 0

while True:
    move = r.choice(["right", "up", "left", "down"])

    if move == "right":
        col += 1
        w.setheading(0)
        w.forward(CELL)

    elif move == "up":
        row += 1
        w.setheading(90)
        w.forward(CELL)

    elif move == "left":
        col -= 1
        w.setheading(180)
        w.forward(CELL)

    elif move == "down":
        row -= 1
        w.setheading(270)
        w.forward(CELL)

    if col == SIZE and row == SIZE:
        w.color("lime green")
        break

    if col < 0 or row < 0 or col > SIZE or row > SIZE:
        w.color("red")
        break

t.mainloop()