from pico2d import *

open_canvas()

boy = load_image('character.png')


def move_top():
    print('Moving top')
    for x in range(0, 800, 10):
        draw_boy(x,550)
    pass


def move_right():
    print('Moving right')
    for y in range(550, 50, -10):
        draw_boy(800, y)
    pass


def move_bottom():
    print('Moving bottom')
    for x in range(800, 0, -10):
        draw_boy(x, 50)
    pass


def move_left():
    print('Moving left')
    for y in range(50, 550, 10):
        draw_boy(0, y)
    pass


def moves_rectangle():
    print('moves_rectangle')
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass


def moves_circle():
    print('moves_circle')
    r = 200
    for deg in range(0, 360, 10):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        draw_boy(x, y)
    pass


def move_p1():
    print('move_p1')
    C = (600, 150)
    A = (400, 550)
    steps = 50
    for i in range(steps + 1):
        x = C[0] + (A[0] - C[0]) * i / steps
        y = C[1] + (A[1] - C[1]) * i / steps
        draw_boy(x, y)
    pass


def move_p2():
    print('move_p2')
    A = (400, 550)
    B = (200, 150)
    steps = 50
    for i in range(steps + 1):
        x = A[0] + (B[0] - A[0]) * i / steps
        y = A[1] + (B[1] - A[1]) * i / steps
        draw_boy(x, y)
    pass


def move_p3():
    print('move_p3')
    B = (200, 150)
    C = (600, 150)
    steps = 50
    for i in range(steps + 1):
        x = B[0] + (C[0] - B[0]) * i / steps
        y = B[1] + (C[1] - B[1]) * i / steps
        draw_boy(x, y)
    pass


def moves_triangle():
    print('moves_triangle')
    move_p1()
    move_p2()
    move_p3()
    pass

def draw_boy(x: float, y: float):
    clear_canvas_now()
    boy.draw_now(x, y)
    delay(0.1)


while True:
    moves_circle()
    moves_rectangle()
    moves_triangle()
    break

close_canvas()
