import turtle
# turtle.setup(width, height, startx, starty) 后两个star指距离屏幕左上角的距离

#一开始海龟会在窗口的中央
# turtle.goto(100, 100)
# turtle.goto(100, -100)
# turtle.goto(-100, -100)
# turtle.goto(-100, 100)
# turtle.goto(0, 0)
#以上坐标为绝对坐标

#相对坐标指海龟相较于上一秒的方向即前后左右
#turtle.fd(D)   沿正前方
#turtle.BK(D)  沿正后方
#turtle.circle(半径，角度)  绘制圆弧
# turtle.fd(100)
# turtle.circle(50, 180)
# turtle.bk(100)

#turtle.seth(绝对角度)  设置海龟的朝向
#turtle.r

#turtle.left(海龟的相对角度)
#turtle.right(海龟的相对角度)

#turtle.pensize(粗细)  设置画笔的粗细
#turtle.pencolor(颜色)  设置画笔的颜色
#turtle.fillcolor(颜色)  设置填充颜色
#turtle.color(颜色1, 颜色2)  设置画笔颜色和填充颜色
#turtle.begin_fill()  开始填充
#turtle.end_fill()  结束填充

#tuetle.penup()  提起画笔
#turtle.pendown()  放下画笔
#turtle.hideturtle()  隐藏海龟


#编写代码时使用 库名.函数名 的方式来调用函数
#可以使用 from 库名 import * 的方式来调用函数

#import 库名 as 库别名

#---------------------------
#以下为练习题

#  01   生成正方形
# import turtle

# turtle.setup(500, 500)
# turtle.goto(100, 0)
# turtle.goto(100, 100)
# turtle.goto(0, 100)
# turtle.goto(0, 0)

# turtle.end_fill()


#   02  生成六边形
# import turtle

# turtle.setup(500, 500)

# for i in range(6):
#     turtle.fd(100)
#     turtle.left(60)


#   03  生成叠边型
# import turtle

# turtle.setup(500, 500)
# for i in range(9):
#     turtle.fd(100)
#     turtle.left(80)


#   04  生成风车
# import turtle as t

# t.pensize(2)
# for i in range(4):
#     t.seth(90*i)
#     t.fd(150)
#     t.right(90)
#     t.circle(-150, 45)
#     t.goto(0,0)

# import turtle as t
# t.pensize(2)
# for i in range(8):
#     t.fd(100)
#     t.left(45)

import turtle as t
t.pensize(2)
for i in range(8):
    t.fd(150)
    t.left(135)