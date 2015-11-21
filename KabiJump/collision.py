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


def update(frame_time):
    kabi.update(frame_time)
    grass.update(frame_time)


    if collide(kabi, grass):
        kabi.on_ground(grass.y + grass.image.h / 3)
        #print('collide')

    # background.update(frame_time)

    for cloud in clouds:
        if kabi.y  > cloud.y:
            if kabi.current_speed < 0:
                if collide(kabi,cloud):
                    kabi.on_ground(cloud.y)
                    #print('collide')

    for ball in balls:
        ball.update(frame_time)

    for ball in balls:
        if collide(kabi,ball):
            ball.stop()
            kabi.death()


def draw(frame_time):
    clear_canvas()
    # background.draw()
    for cloud in clouds:
        cloud.draw()
        cloud.draw_bb()
    kabi.draw()
    kabi.draw_bb()

    grass.draw()
    grass.draw_bb()

    for ball in balls:
        ball.draw()
        ball.draw_bb()

    update_canvas()
