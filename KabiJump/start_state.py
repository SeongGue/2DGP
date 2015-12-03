import game_framework
import title_state
from pico2d import *


name = "StartState"
image = None
logo = None
logo_time = 0.0


def enter():
    global image, logo
    open_canvas()
    image = load_image('resource\\image\\kpu_credit.png')
    logo = load_image('resource\\image\\GameGrade_Image.png.jpg')

def exit():
    global image, logo
    del(image)
    del(logo)

def update(frame_time):
    global logo_time

    if(logo_time > 6.0):
        logo_time = 0
        game_framework.push_state(title_state)
    logo_time += 0.01

def draw(frame_time):
    global image, logo
    clear_canvas()
    image.draw(400, 300)
    logo.draw(70, 520)
    update_canvas()

def handle_events(frame_time):
    events = get_events()


def pause(): pass


def resume(): pass




