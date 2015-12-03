from pico2d import *

import game_framework
import title_state

from kabi import Kabi
from cloud import Cloud
from background import Background, Grass
from obstruction import BigBall
from ui import Ui

name = "MainState"

kabi = None
clouds = None
top_clouds = None
background = None
balls = None
grass = None
ui = None

OFF, ON = 0, 1

change_field = OFF

COL_CLOUDS = 0
CHECK_COL_CLOUD = 0

score = 0
save_score = 0


def create_world():
    global kabi, clouds, background, balls, grass, top_grass, ui
    kabi = Kabi()
    clouds = [Cloud(0) for i in range(10)]
    background = Background(800, 1064)
    balls = [BigBall() for i in range (10)]
    grass = Grass(400, 0)
    top_grass = Grass(400, 600)
    ui = Ui()


def destroy_world():
    global kabi, clouds, background, balls, grass, top_grass, ui

    del(kabi)
    clouds.clear()
    del(background)
    balls.clear()
    del(grass)
    del(top_grass)
    del(ui)


def enter():
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
            game_framework.push_state(title_state)
        else:
            kabi.handle_event(event)

def update(frame_time):
    global change_field, COL_CLOUDS, CHECK_COL_CLOUD, save_score, score

    if collide(kabi, top_grass):
        if COL_CLOUDS == 10:
            change_field = ON
            if save_score == 0:
                score += kabi.y
                save_score += 1


    if change_field == ON:
        kabi.change_field(frame_time)
        grass.change_field(frame_time)
        top_grass.change_field(frame_time)
        background.update(frame_time)
        for ball in balls:
            ball.y = -25
        for cloud in clouds:
            cloud.update(frame_time)
        if kabi.y < 50:
            change_field = OFF
            for cloud in clouds:
                cloud.regen()
            for ball in balls:
                ball.regen()
            grass.y = 0
            top_grass.y = 600
            kabi.up_down = True
            save_score = 0


    if change_field == OFF:
        kabi.update(frame_time)

        if collide(kabi, grass):
            kabi.on_ground(grass.y + grass.image.h / 3)


        for cloud in clouds:
            if collide(kabi,cloud):
                cloud.change_cloud()
                if kabi.y  > cloud.y:
                    if kabi.current_speed < 0:
                        if collide(kabi,cloud):
                            kabi.on_ground(cloud.y)

        for ball in balls:
            ball.update(frame_time)

        for ball in balls:
            if collide(kabi,ball):
                ball.stop()
                kabi.death()

        for cloud in clouds:
            if cloud.cloud_state == cloud.AFT_COL:
                CHECK_COL_CLOUD += 1

        COL_CLOUDS = CHECK_COL_CLOUD
        CHECK_COL_CLOUD = 0

        ui.update(frame_time, score + kabi.y)




def draw(frame_time):
    clear_canvas()
    background.draw()

    for cloud in clouds:
        cloud.draw()
        #cloud.draw_bb()

    kabi.draw()
    #kabi.draw_bb()

    grass.draw()
    #grass.draw_bb()

    top_grass.draw()
    #top_grass.draw_bb()

    for ball in balls:
        ball.draw()
        #ball.draw_bb()

    ui.draw_font()
    ui.draw_gauge_bar(kabi.x, kabi.y, kabi.gauge_ctrl(frame_time))

    update_canvas()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False
    return True