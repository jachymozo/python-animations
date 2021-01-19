from turtle import forward, left, right, speed, exitonclick
speed(3000)
for i in range(18):

    for j in range(360):
        forward(1)
        left(1)

    left(20)
for i in range(18):

    for j in range(180):
        forward(2)
        left(2)

    left(20)
for i in range(6):

    for j in range(6):
        forward(100)
        left(60)

    left(60)

exitonclick()
