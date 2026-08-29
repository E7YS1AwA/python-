# import turtle
# turtle.setup(650, 350, 200, 200)
# turtle.penup()
# turtle.fd(-250)
# turtle.pendown()
# turtle.pensize(25)
# turtle.pencolor("purple")
# turtle.seth(-40)
# for i in range(4):
#     turtle.circle(40, 80)
#     turtle.circle(-40, 80)
# turtle.circle(40, 80/2)
# turtle.fd(40)
# turtle.circle(16, 160)
# turtle.fd(40 * 2/3)
# turtle.done()

 #---------------
#改进
from turtle import*
setup(650, 350, 200, 200)
penup()
fd(-250)
pendown()
pensize(25)
pencolor("purple")
seth(-40)
for i in range(4):
    circle(40, 80)
    circle(-40, 80)
circle(40, 80/2)
fd(40)    
circle(16, 160)
fd(40 * 2/3)
done()