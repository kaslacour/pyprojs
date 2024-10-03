from turtle import Turtle, Screen

#while True:

s = Screen()
s.canvwidth
#s.onkey()
Aya = Turtle()
Aya.shape('triangle')
Aya.fillcolor(1,0,0)
Aya.color(1,0,0)
Aya.speed(1)

for i in range(10):
    None

Aya.begin_fill()
Aya.circle(5)
Aya.end_fill()
Aya.forward(100)


def left():
    Aya.setheading(180)

def right():
    Aya.setheading(0)

def red():
    Aya.color('red')

def green():
    Aya.color('green')

def blue():
    Aya.color('blue')

def move():
    Aya.forward(25)

s.onkey(left, "Left")
s.onkey(right, "Right")

s.onkey(red,"r")
s.onkey(green,'g')
s.onkey(blue,"b")

s.listen()


s.mainloop()