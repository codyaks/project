import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(500,500)
t=turtle.Turtle()
size=0
while True:
    for i in range(4):
        t.forward(size+1)
        t.left(90)
        size=size-5
    size=size+1