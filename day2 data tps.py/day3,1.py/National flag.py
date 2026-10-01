import turtle
import math

screen = turtle.Screen()
screen.setup(900, 650)
screen.bgcolor("white")
screen.title("🇮🇳 Happy Independence Day 🇮🇳")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# ---------------- FLAG ----------------

# Flag position
x = -300
y = 180
width = 600
height = 120

# Saffron
t.penup()
t.goto(x, y)
t.pendown()
t.fillcolor("#FF9933")
t.begin_fill()
for _ in range(2):
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
t.end_fill()

# White
t.penup()
t.goto(x, y - height)
t.pendown()
t.fillcolor("white")
t.begin_fill()
for _ in range(2):
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
t.end_fill()

# Green
t.penup()
t.goto(x, y - 2 * height)
t.pendown()
t.fillcolor("#138808")
t.begin_fill()
for _ in range(2):
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
t.end_fill()

# ---------------- ASHOKA CHAKRA ----------------

cx = 0
cy = 60
radius = 45

t.color("#000080")
t.pensize(3)

# Outer circle
t.penup()
t.goto(cx, cy - radius)
t.setheading(0)
t.pendown()
t.circle(radius)

# 24 spokes
for i in range(24):
    angle = math.radians(i * 15)

    x1 = cx + radius * math.cos(angle)
    y1 = cy + radius * math.sin(angle)

    t.penup()
    t.goto(cx, cy)
    t.pendown()
    t.goto(x1, y1)

# ---------------- FLAG POLE ----------------

t.color("#555555")
t.pensize(8)

t.penup()
t.goto(-305, 180)
t.pendown()
t.goto(-305, -250)

# Pole base
t.pensize(5)
t.goto(-350, -250)
t.goto(-260, -250)

# ---------------- MESSAGE ----------------

t.penup()
t.goto(0, -310)
t.color("#222222")

t.write(
    "HAPPY INDEPENDENCE DAY",
    align="center",
    font=("Georgia", 28, "bold")
)

t.penup()
t.goto(0, -350)
t.color("#555555")

t.write(
    "Proud to be Indian 🇮🇳",
    align="center",
    font=("Georgia", 18, "italic")
)

turtle.done()