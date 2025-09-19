from pico2d import *

open_canvas()

boy = load_image('character.png')

def moves_rectangle():
    print('moves_rectangle')
    pass


def moves_circle():
    print('moves_circle')
    clear_canvas_now()
    boy.draw_now(400,300)
    delay(0.1)
    pass


while True:
    moves_rectangle()
    moves_circle()
    break

close_canvas()
