from pico2d import *

import game_framework
import title_state
import os
import random

from kabi import Kabi
from cloud import Cloud
from background import Background, Grass
from obstruction import BigBall, UFO
from ui import Ui
from item import Shield

name = "MainState"

player = None
clouds = None
top_clouds = None
background = None
balls = None
grass = None
ui = None
shield = None
ufos = None


OFF, ON = 0, 1

change_field = OFF

COL_CLOUDS = 0
CHECK_COL_CLOUD = 0
##점수 관련 변수
score = 0
save_score = 0
save_time = 0
game_level = 0

gen_ball = 3

cloud_data_file = open('resource\\txt\\cloud_data.txt', 'r')
cloud_data = json.load(cloud_data_file)
cloud_data_file.close()

cloud_model = 0


def create_world():
    global player, clouds, background, balls, grass, top_grass, ui, shield, cloud_model
    player = Kabi()
    #clouds = cloud_pattern(cloud_model)
    clouds = cloud_pattern(cloud_model)
    cloud_model += 1
    background = Background(800, 1064)
    balls = [BigBall() for i in range (5)]
    grass = Grass(400, 0)
    top_grass = Grass(400, 600)
    ui = Ui()
    shield = Shield()



def destroy_world():
    global player, clouds, background, balls, grass, top_grass, ui, shield, ufos

    del(player)
    del(background)
    del(clouds)
    del(balls)
    del(grass)
    del(top_grass)
    del(ui)
    del(shield)
    del(ufos)


def enter():
    create_world()


def exit():
    pass



def pause():
    pass


def resume():
    pass


def handle_events(frame_time):
    global player
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        else:
            player.handle_event(event)

def update(frame_time):
    global change_field, COL_CLOUDS, CHECK_COL_CLOUD, save_score, score, save_time, game_level, balls, ufos, gen_ball, clouds, cloud_model

    if collide(player, top_grass):
        if COL_CLOUDS == 10:
            change_field = ON
            if save_score == 0:
                score += player.y
                save_score += 1
                if game_level < 15:
                    game_level += 1
                    balls = [BigBall() for i in range(5 + (game_level % 10))]
                    if game_level % gen_ball == 0:
                        ufos = [UFO() for i in range((int)(game_level / gen_ball))]
            if game_level > gen_ball:
                for ufo in ufos:
                    ufo.x = random.randint(100, 700)
                    ufo.y = random.randint(300, 500)




    if change_field == ON:
        player.change_field(frame_time)
        grass.change_field(frame_time)
        top_grass.change_field(frame_time)
        background.update(frame_time)
        for ball in balls:
            ball.y = -25
        for cloud in clouds:
            cloud.update(frame_time)
        if player.y < 50:
            change_field = OFF
            clouds = cloud_pattern(cloud_model % 10)
            cloud_model += 1
            for ball in balls:
                ball.regen()
            grass.y = 0
            top_grass.y = 600
            player.up_down = True
            save_score = 0


    if change_field == OFF:
        player.update(frame_time)

        if collide(player, grass):
            player.on_ground(grass.y + grass.image.h / 3)


        for cloud in clouds:
            if collide(player,cloud):
                cloud.change_cloud()
                if player.y  > cloud.y:
                    if player.current_speed < 0:
                        if collide(player,cloud):
                            player.on_ground(cloud.y)

        for ball in balls:
            ball.update(frame_time)

        for ball in balls:
            if collide(player,ball):
                if shield.shield_num == 0:
                    record_score()
                    player.death()
                    score = 0
                    save_time = get_time()
                    game_level = 0
                    cloud_model = 0
                    clouds.clear()
                else:
                    ball.y = 0
                    shield.shield_num -= 1

        for cloud in clouds:
            if cloud.cloud_state == cloud.AFT_COL:
                CHECK_COL_CLOUD += 1

        ui.update(frame_time, score + player.y, save_time)
        shield.update(frame_time)

        if collide(player, shield):
            shield.eat_shield()

        COL_CLOUDS = CHECK_COL_CLOUD
        CHECK_COL_CLOUD = 0

        if game_level >= gen_ball:
            for ufo in ufos:
                if collide(player, ufo):
                    record_score()
                    player.death()
                    score = 0
                    save_time = get_time()
                    game_level = 0
                    cloud_model = 0
                    clouds.clear()

            for ufo in ufos:
                ufo.update(frame_time)





def draw(frame_time):
    clear_canvas()
    background.draw()

    for cloud in clouds:
        cloud.draw()
        #cloud.draw_bb()

    player.draw()
    #kabi.draw_bb()

    grass.draw()
    #grass.draw_bb()

    top_grass.draw()
    #top_grass.draw_bb()

    for ball in balls:
        ball.draw()
        #ball.draw_bb()

    ui.draw_font()
    ui.draw_gauge_bar(player.x, player.y, player.gauge_ctrl(frame_time))
    shield.draw()
    if game_level >= gen_ball:
        for ufo in ufos:
            ufo.draw()


    update_canvas()


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if bottom_a > top_b: return False
    if top_a < bottom_b: return False
    return True

def record_score():
    global score

    record = {"score":score + player.y }

    score_list = []
    if os.path.exists('score.txt'):
        with open('score.txt', 'r') as f:
            score_list = json.load(f)

    score_list.append(record)
    with open('score.txt', 'w') as f:
        json.dump(score_list, f)

def cloud_pattern(pattern_num):
    model = {
        0 : 'MODEL 1',
        1 : 'MODEL 2',
        2 : 'MODEL 3',
        3 : 'MODEL 4',
        4 : 'MODEL 5',
        5 : 'MODEL 6',
        6 : 'MODEL 7',
        7 : 'MODEL 8',
        8 : 'MODEL 9',
        9 : 'MODEL 10'
    }

    cloud_data_file = open('resource\\txt\\cloud_data.txt', 'r')
    cloud_data = json.load(cloud_data_file)
    cloud_data_file.close()
    clouds = []
    for name in cloud_data[model[pattern_num]]:
        cloud = Cloud()
        cloud.name = name
        cloud.x = cloud_data[model[pattern_num]][name]['x']
        cloud.y = cloud_data[model[pattern_num]][name]['y']
        clouds.append(cloud)
    return clouds