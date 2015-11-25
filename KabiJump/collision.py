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
top_clouds = None
background = None
balls = None
grass = None

OFF, ON = 0, 1

change_field = OFF


def create_world():
    global kabi, clouds, background, balls, grass, top_grass
    kabi = Kabi()
    clouds = [Cloud(0) for i in range(10)]
    background = Background(800, 1064)
    balls = [BigBall() for i in range (10)]
    grass = Grass(400, 0)
    top_grass = Grass(400, 600)


def destroy_world():
    global kabi, clouds, background, balls, grass, top_grass

    del(kabi)
    del(clouds)
    del(background)
    del(balls)
    del(grass)
    del(top_grass)


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
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        else:
            kabi.handle_event(event)


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False
    return True


def update(frame_time):
    global change_field

    if collide(kabi, top_grass):
            change_field = ON

    if change_field == ON:
        kabi.change_field(frame_time)
        grass.change_field(frame_time)
        top_grass.change_field(frame_time)
        background.update(frame_time)
        for cloud in clouds:
            cloud.update(frame_time, change_field)
        if kabi.y < 50:
            change_field = OFF
            grass.y = 0
            kabi.up_down = True


    if change_field == OFF:
        kabi.update(frame_time)

        if collide(kabi, grass):
            kabi.on_ground(grass.y + grass.image.h / 3)


        for cloud in clouds:
            if kabi.y  > cloud.y:
                if kabi.current_speed < 0:
                    if collide(kabi,cloud):
                        kabi.on_ground(cloud.y)

        for cloud in clouds:
            cloud.update(frame_time, change_field)

        for ball in balls:
            ball.update(frame_time)

        for ball in balls:
            if collide(kabi,ball):
                ball.stop()
                kabi.death()


def draw(frame_time):
    clear_canvas()
    background.draw()

    for cloud in clouds:
        cloud.draw()
        cloud.draw_bb()

    kabi.draw()
    kabi.draw_bb()

    grass.draw()
    grass.draw_bb()

    top_grass.draw()
    top_grass.draw_bb()

    for ball in balls:
        ball.draw()
        ball.draw_bb()

    update_canvas()
