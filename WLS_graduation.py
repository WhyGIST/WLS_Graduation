import turtle as t
import time


# 画笔位置落点
def my_goto(x, y):
    t.penup()
    t.goto(x + 300, y - 300)
    t.pendown()


# 星星位置落点
def star_goto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# 画星星
def drawStarSingle():
    t.speed(0)  # 参数范围：1-10，若写0则为最快，也可以写"fastest"
    t.color("pink", 'pink')  # 定义画笔颜色为粉色
    # t.pu()  # 提笔，pu=penup
    # t.setx(r.randint(-360, 360))  # 定义x坐标，随机从-350到350之间选择
    # t.sety(r.randint(-360, 360))  # 定义y坐标，
    # t.pd()  # 落笔，pd=pendown
    n = 32
    t.begin_fill()
    t.left(126)
    for i in range(5):
        t.forward(n / 5)
        t.right(144)
        t.forward(n / 5)
        t.left(72)
    t.end_fill()
    t.right(126)


# WLS星星背景
def drawStarWLS():
    list_loc = [
        # W
        [-360, 150], [-347, 90], [-334, 30], [-321, -30], [-308, -90], [-295, -150],
        [-282, -90], [-269, -30], [-256, 30], [-243, 90], [-230, 150],
        [-217, 90], [-204, 30], [-191, -30], [-178, -90], [-165, -150],
        [-152, -90], [-139, -30], [-126, 30], [-113, 90], [-100, 150],
        # L
        [-60, 150], [-64, 90], [-68, 30], [-72, -30], [-76, -90], [-80, -150],
        [-15, -140], [45, -140], [110, -150],
        # S
        [340, 120], [295, 140], [240, 150], [180, 123], [170, 70],
        [205, 35], [240, 0], [275, -35],
        [310, -70], [340, -118], [290, -142], [235, -150], [170, -120]
    ]
    for i in list_loc:
        star_goto(i[0], i[1])
        drawStarSingle()


# 头型
def head():
    t.pencolor('black')
    t.penup()
    my_goto(0, 0)
    t.circle(75, 40)
    t.pendown()
    t.fillcolor('#00a0de')
    t.begin_fill()
    t.circle(75, 280)
    t.end_fill()


# 围巾
def scarf():
    t.fillcolor('#e70010')
    t.begin_fill()
    t.seth(0)
    t.fd(100)
    t.circle(-2.5, 90)
    t.fd(5)
    t.circle(-2.5, 90)
    t.fd(103.5)
    t.circle(-2.5, 90)
    t.fd(5)
    t.circle(-2.5, 90)
    t.end_fill()


# 脸
def face():
    t.fd(91.5)
    t.lt(45)
    t.fillcolor('#ffffff')
    t.begin_fill()
    t.circle(60, 100)
    t.seth(180)
    # print(pos())
    t.fd(60.5)
    t.pendown()
    t.seth(215)
    t.circle(60, 100)
    t.end_fill()
    t.pu()
    t.goto(63.56 / 2 + 300, (218.24 / 2 - 300))
    t.seth(90)
    t.pendown()
    eyes()
    t.seth(180)
    t.penup()
    t.fd(30)
    t.pendown()
    t.seth(90)
    eyes()


# 眼眶
def eyes():
    t.fillcolor("#ffffff")
    t.begin_fill()
    t.tracer(False)
    a = 1.78
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            t.lt(3)
            t.fd(a)
        else:
            a += 0.05
            t.lt(3)
            t.fd(a)
    t.tracer(True)
    t.end_fill()


# 瞳孔
def black_eyes():
    t.seth(0)
    my_goto(-10, 97.5)
    t.fillcolor('#000000')
    t.begin_fill()
    t.circle(6.5)
    t.end_fill()

    t.pensize(3)
    my_goto(10, 102.5)
    t.seth(75)
    t.circle(-5, 150)
    t.pensize(1.5)

    my_goto(-8.5, 100)
    t.seth(0)
    t.fillcolor('#ffffff')
    t.begin_fill()
    t.circle(2.5)
    t.end_fill()

    t.pensize(1)


# 鼻子
def nose():
    my_goto(-6, 72)
    t.seth(315)
    t.fillcolor('#e70010')
    t.begin_fill()
    t.circle(10)
    t.end_fill()


# 嘴巴
def mouth():
    my_goto(3, 70)
    t.seth(270)
    t.fd(45)
    t.seth(0)
    t.circle(60, 50)
    t.seth(230)
    t.circle(-60, 100)


# 胡须
def beard():
    my_goto(-16, 67.5)
    t.seth(165)
    t.fd(30)

    my_goto(-16, 62.5)
    t.seth(180)
    t.fd(30)

    my_goto(-16, 57.5)
    t.seth(193)
    t.fd(30)

    my_goto(18.5, 67.5)
    t.seth(15)
    t.fd(30)

    my_goto(18.5, 62.5)
    t.seth(0)
    t.fd(30)

    my_goto(18.5, 57.5)
    t.seth(-13)
    t.fd(30)


# 铃铛
def bell():
    my_goto(-51.71, 7.54)
    t.pu()
    t.seth(0)
    t.fd(45)
    t.pd()
    t.seth(70)
    t.fillcolor('#ffd200')
    # print(pos())
    t.begin_fill()
    t.circle(-10)
    t.end_fill()
    t.seth(170)
    t.fillcolor('#ffd200')
    t.begin_fill()
    t.circle(-1, 180)
    t.seth(10)
    t.circle(-50, 22)
    t.circle(-1, 180)
    t.seth(180 - 10)
    t.circle(50, 22)
    t.end_fill()
    my_goto(-6.71, 7.55)
    t.seth(250)
    t.circle(10, 110)
    t.seth(90)
    t.fd(7.5)
    t.dot(5)
    my_goto(-300, 300)


# 画哆啦A梦
def drawDoraemon():
    # 头部
    head()
    # 围脖
    scarf()
    # 脸
    face()
    # 画瞳孔
    black_eyes()
    # 红鼻子
    nose()
    # 嘴巴
    mouth()
    # 胡须
    beard()
    # 铃铛
    bell()
    t.hideturtle()


def writeName():
    info = ['To', ' WD ', '&', ' Tina:']
    # info = ['To', 'Xiaoman_MBY:']
    t.pu()
    t.goto(0, 15)
    t.seth(0)
    t.fd(-340)
    for i in info:
        distance = len(i) * 32 + 18
        t.write(i, align='left', font=("Comic Sans MS", 40, "normal"))
        t.fd(distance)


def writeGraduation():
    info = ['Happy', 'Graduation!']
    t.pu()
    t.goto(0, -45)
    t.fd(-160)
    for i in info:
        t.write(i, font=("Comic Sans MS", 40, "normal"))
        t.fd(len(i) * 38)


if __name__ == '__main__':
    t.screensize(800, 800, bg='white')
    t.title("~WLS毕业快乐WLS~")
    t.speed(0)
    time.sleep(5)
    drawStarWLS()
    drawDoraemon()
    t.hideturtle()
    t.speed(7)
    writeName()
    writeGraduation()
    t.done()
