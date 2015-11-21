from pico2d import *

import game_framework
import title_state

from kabi import Kabi # import Boy class from boy.py
from cloud import Cloud
from background import Background, Grass
from obstruction import BigBall

name = "collision"

kabi = None
clouds = None
background = None
balls = None
grass = None

PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
SCROLL_SPEED_KMPH = 80.0                    # Km / Hour
SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

ON, OFF = 0, 1
SCROLL_DOWN = OFF

scroll_high = 0

def create_world():
    global kabi, clouds, background, balls, grass
    kabi = Kabi()
    clouds = [Cloud() for i in range(10)]
    background = Background(800, 1064)
    balls = [BigBall() for i in range (10)]
    grass = Grass()

def destroy_world():
    global kabi, clouds, background, balls

    del(kabi)
    del(clouds)
    del(background)
    del(balls)
    del(grass)



def enter():
    open_canvas()
    game_framework.reset_time()
    create_world()


def exit():
    destroy_world()
    close_canvas()


def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global kabi
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        else:
            kabi.handle_event(event)
            background.handle_event(event)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False
    return True

def high_check(a, b):
    # if a.y  > b.y:
    #     return True
    # else:
    #     return False
    pass




def update(frame_time):
    #global SCROLL_DOWN, scroll_high
    kabi.update(frame_time)
    grass.update(frame_time)

    if collide(kabi, grass):
        kabi.on_ground(grass.y + grass.image.h / 3)
    # background.update(frame_time)
    # # for ball in balls:
    # #     ball.update(frame_time)
    # for cloud in clouds:
    #     if kabi.up_down_state == kabi.DOWN:
    #         if collide(kabi,cloud):
    #             if high_check(kabi, cloud):
    #                 kabi.stop()
    #
    # if kabi.y > 400:
    #     SCROLL_DOWN = ON
    # elif kabi.y < 400:
    #     SCROLL_DOWN = OFF
    #
    # if SCROLL_DOWN == ON:
    #     scroll_high += SCROLL_SPEED_PPS * frame_time
    #
    # for cloud in clouds:
    #     cloud.update(frame_time)
    #
    #
    # for ball in balls:
    #     ball.update(frame_time)
    #
    # for ball in balls:
    #     if collide(kabi,ball):
    #         ball.stop()
    #         kabi.death()







def draw(frame_time):
    global scroll_high
    clear_canvas()
    # background.draw()
    # for cloud in clouds:
    #     cloud.draw(scroll_high)
    #     cloud.draw_bb()
    kabi.draw()
    kabi.draw_bb()

    grass.draw()
    grass.draw_bb()
    #
    # for ball in balls:
    #     ball.draw()
    #     ball.draw_bb()

    update_canvas()
