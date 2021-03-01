import graphics
from graphics import *

spisok = []

file = open('markdown.md', 'r', encoding="utf-8")

actions = file.readline().split(',')
actions = [action.rstrip() for action in actions]

x1 = 100
y1 = 150
x2 = 250
y2 = 200
a = 175
b = 175


# draw actions
win = GraphWin("Окно для графики", 1000, 1000)
for action in actions:
    obj = Rectangle(Point(x1, y1), Point(x2, y2))
    msg = Text(Point(a, b), action)
    obj.draw(win)
    msg.draw(win)
    x1 += 200
    y1 += 100
    x2 += 200
    y2 += 100
    a += 200
    b += 100

#return params in basic values
x1 = 100
y1 = 150
x2 = 250
y2 = 200
a = 175
b = 175


# action's arrows
def get_index(actn):
    for action in actn:
        num = actions.index(action.rstrip())
    return num


line = file.readline()
while line != 'end links':
    conns = line.split('->')
    frst = get_index(conns[0:1])
    scnd = get_index(conns[1:2])
    p1 = Point(x2 + frst * 200, b + frst * 100)
    p2 = Point(x2 + frst * 200 + 25, b + frst * 100)
    p3 = Point(x2 + frst * 200 + 25, b + scnd * 100)
    p4 = Point(x1 + scnd * 200, b + scnd * 100)
    line1 = Line(p1, p2)
    line2 = Line(p2, p3)
    line3 = Line(p3, p4)
    arw1 = Line(Point(p4.getX() - 10, p4.getY() - 10), p4)
    arw2 = Line(Point(p4.getX() - 10, p4.getY() + 10), p4)
    line1.draw(win)
    line2.draw(win)
    line3.draw(win)
    arw1.draw(win)
    arw2.draw(win)
    line = file.readline().rstrip()


#enter
line = file.readline().rstrip()


def draw_arrow(p1, p2):
    line1 = Line(Point(p1.getX() + 25, p1.getY()), p2)
    arr1 = Line(Point(p2.getX() - 5, p2.getY() - 5), p2)
    arr2 = Line(Point(p2.getX() - 5, p2.getY() + 5), p2)
    line1.draw(win)
    arr1.draw(win)
    arr2.draw(win)

def draw_arrow2(p1, p2):
    line1 = Line(Point(p1.getX() + 25, p1.getY()), p2)
    arr1 = Line(Point(p2.getX() - 5, p2.getY() - 5), p2)
    arr2 = Line(Point(p2.getX() + 5, p2.getY() - 5), p2)
    line1.draw(win)
    arr1.draw(win)
    arr2.draw(win)

def draw_arrow3(p1, p2):
    line1 = Line(Point(p1.getX() + 25, p1.getY()), p2)
    arr1 = Line(Point(p2.getX() + 5, p2.getY() + 5), p2)
    arr2 = Line(Point(p2.getX() - 5, p2.getY() + 5), p2)
    line1.draw(win)
    arr1.draw(win)
    arr2.draw(win)

while line != 'end enter':
    entrs = line.split(',')
    y12 = (y1 + (y2 - y1) / 4)
    y34 = (y2 - (y2 - y1) / 4)
    p1 = Point(25, y12)
    p2 = Point(x1, y12)
    p3 = Point(25, y34)
    p4 = Point(x1, y34)
    entr1 = Text(p1, entrs[0:1])
    entr2 = Text(p3, entrs[1:2])
    entr1.draw(win)
    entr2.draw(win)
    draw_arrow(p1, p2)
    draw_arrow(p3, p4)

    line = file.readline().rstrip()

line = file.readline().rstrip()

while line != 'end control':
    entrs = line.split(',')
    msg = Text(Point(190, 100), entrs[0:1])
    msg2 = Text(Point(130, 100), entrs[1:2])
    msg.draw(win)
    msg2.draw(win)
    p1 = Point(105, 100)
    p2 = Point(130, y1)
    p3 = Point(160, 100)
    p4 = Point(185, y1)
    draw_arrow2(p1, p2)
    draw_arrow2(p3, p4)

    line = file.readline().rstrip()

line = file.readline().rstrip()

while line != "end doing":
    entrs = line.split(',')
    msg = Text(Point(190, 260), entrs[0:1])
    msg2 = Text(Point(130, 260), entrs[1:2])
    msg.draw(win)
    msg2.draw(win)
    p1 = Point(105, 250)
    p2 = Point(130, 200)
    p3 = Point(160, 250)
    p4 = Point(185, 200)
    draw_arrow3(p1, p2)
    draw_arrow3(p3, p4)

    line = file.readline().rstrip()

#exit
s_exit = file.readline()
y = b + (len(actions) - 1) * 100
x_exit = x2 + (len(actions) - 1) * 200 + 100
x2_exit = x2 + (len(actions) - 1) * 200
p1 = Point(x_exit - 25, y)
exit = Text(Point(x_exit, y), s_exit)
line = Line(Point(x2_exit, y), p1)
arr = Line (Point(p1.getX() - 10, p1.getY() - 10), p1)
arr2 = Line (Point(p1.getX() - 10, p1.getY() + 10), p1)
exit.draw(win)
line.draw(win)
arr.draw(win)
arr2.draw(win)

win.getMouse()
win.close()
