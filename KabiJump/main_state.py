from pico2d import *
import random
import game_framework
import title_state

kabi = None
background = None
cloud = None

class Cloud:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint(0, 600)
        if Cloud.image == None:
            Cloud.image = load_image('cloud_one.png')
    def draw(self):
        self.image.draw(self.x, self.y)

class BackGround:
    global kabi
    def __init__(self):
        self.background_one = load_image('background_one.png')
        self.background_two = load_image('background_two.png')
        self.y1 = 536
        self.y2 = 1602

    def update(self):
        if(kabi.y >300 and kabi.direction_up_state == True):
            self.y1 -= 10
            self.y2 -= 10
        if(self.y1 < -600):
            self.y1 = 1506
        elif(self.y2 < -500):
            self.y2 = 1602

    def draw(self):
        self.background_one.draw(0, self.y1)
        self.background_two.draw(0, self.y2)

class Kabi:

    STAND_STATE, WALK_STATE, JUMP_STATE, FLY_STATE, FALL_STATE = 0, 1, 2, 3, 4
    LEFT, RIGHT = 0, 1

    def handle_stand(self):
        pass

    def handle_walk(self):
        pass

    def handle_jump(self):
        self.y += self.jump_direction
        if(self.y > 90):
            self.jump_direction -= 10
        elif(self.y < 90):
            self.jump_direction = 40
            self.y = 90
            self.act_state = self.STAND_STATE
            if(self.direction_left_state == True or self.direction_right_state == True):
                self.act_state = self.WALK_STATE

    def handle_fly(self):
        if(self.direction_up_state == True and self.y < 400):
            self.y += 10
        elif(self.direction_down_state == True):
            self.y -= 10

    def handle_fall(self):
        self.y -= self.fall_direction
        if(self.y > 90):
            self.fall_direction += 5
        elif(self.y < 90):
            self.fall_direction = 20
            self.jump_direction = 40
            self.y = 90
            self.act_state = self.STAND_STATE
            if(self.direction_left_state == True or self.direction_right_state == True):
                self.act_state = self.WALK_STATE

    def __init__(self):
        self.direction_left_state = False
        self.direction_right_state = False
        self.direction_up_state = False
        self.direction_down_state = False
        self.save_direction = self.LEFT
        self.act_state = self.STAND_STATE
        self.Lidle = load_image('Lidle_kabi.png')
        self.Ridle = load_image('Ridle_kabi.png')
        self.Lwalk = load_image('Lwalk_kabi.png')
        self.Rwalk = load_image('Rwalk_kabi.png')
        self.Ljump = load_image('Ljump_kabi.png')
        self.Rjump = load_image('Rjump_kabi.png')
        self.LFly = load_image('Lfly_kabi.png')
        self.RFly = load_image('Rfly_kabi.png')

        self.walk_frame = 0
        self.jump_frame = 0
        self.fly_frame = 0

        self.jump_direction = 40
        self.fall_direction = 20

        self.x, self.y = 400, 90

    handle_state = {
        STAND_STATE : handle_stand,
        WALK_STATE : handle_walk,
        JUMP_STATE : handle_jump,
        FLY_STATE : handle_fly,
        FALL_STATE : handle_fall
    }

    def update(self):
        self.walk_frame = frame = (self.walk_frame + 1) % 10
        self.jump_frame = (self.jump_frame + 1) % 8
        self.fly_frame = (self.fly_frame + 1) % 7

        if(self.direction_left_state == True):
            if(self.x > 0):
                self.x -= 10
        elif(self.direction_right_state == True):
            if(self.x < 800):
                self.x += 10
        # if(self.direction_up_state == True):
        #     self.y += 10
        # elif(self.direction_down_state == True):
        #     self.y -= 10

        self.handle_state[self.act_state](self)

    def draw(self):
        if(self.save_direction == self.LEFT):
            if(self.act_state == self.STAND_STATE):
                self.Lidle.draw(self.x, self.y)
            elif(self.act_state == self.WALK_STATE):
                self.Lwalk.clip_draw((self.walk_frame + 1) * 51, 0, 51, 50, self.x, self.y)
            elif(self.act_state == self.JUMP_STATE):
                self.Ljump.clip_draw(self.jump_frame * 50, 0, 40, 50, self.x, self.y)
            elif(self.act_state == self.FLY_STATE):
                self.LFly.clip_draw(self.fly_frame * 55, 0, 55, 50, self.x, self.y)
            elif(self.act_state == self.FALL_STATE):
                self.Lwalk.clip_draw(0, 0, 51, 50, self.x, self.y)

        elif(self.save_direction == self.RIGHT):
            if(self.act_state == self.STAND_STATE):
                self.Ridle.draw(self.x, self.y)
            elif(self.act_state == self.WALK_STATE):
                self.Rwalk.clip_draw(self.walk_frame * 51, 0, 51, 50, self.x, self.y)
            elif(self.act_state == self.JUMP_STATE):
                self.Rjump.clip_draw(self.jump_frame * 48, 0, 40, 50, self.x, self.y)
            elif(self.act_state == self.FLY_STATE):
                self.RFly.clip_draw(self.fly_frame * 55, 0, 55, 50, self.x, self.y)
            elif(self.act_state == self.FALL_STATE):
                self.Rwalk.clip_draw(512, 0, 51, 50, self.x, self.y)

def handle_events():
    global kabi
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)

        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            kabi.save_direction = kabi.LEFT
            kabi.direction_left_state = True
            kabi.direction_right_state = False
            if(kabi.act_state != kabi.JUMP_STATE and kabi.act_state != kabi.FLY_STATE and kabi.act_state != kabi.FALL_STATE):
                kabi.act_state = kabi.WALK_STATE

        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            kabi.save_direction = kabi.RIGHT
            kabi.direction_left_state = False
            kabi.direction_right_state = True
            if(kabi.act_state != kabi.JUMP_STATE and kabi.act_state != kabi.FLY_STATE and kabi.act_state != kabi.FALL_STATE):
                kabi.act_state = kabi.WALK_STATE

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            kabi.direction_left_state = False
            if(kabi.act_state != kabi.JUMP_STATE and kabi.act_state != kabi.FLY_STATE and kabi.act_state != kabi.FALL_STATE and kabi.direction_right_state == False):
                kabi.act_state = kabi.STAND_STATE

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            kabi.direction_right_state = False
            if(kabi.act_state != kabi.JUMP_STATE and kabi.act_state != kabi.FLY_STATE and kabi.act_state != kabi.FALL_STATE and kabi.direction_left_state == False):
                kabi.act_state = kabi.STAND_STATE

        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE) and ((kabi.act_state == kabi.JUMP_STATE) or (kabi.act_state == kabi.FALL_STATE)):
            kabi.act_state = kabi.FLY_STATE

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_SPACE) and (kabi.act_state == kabi.FLY_STATE):
            kabi.act_state = kabi.FALL_STATE
            kabi.direction_up_state = False
            kabi.direction_down_state = False

        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            kabi.act_state = kabi.JUMP_STATE

        elif((event.type, event.key) == (SDL_KEYDOWN, SDLK_UP) and (kabi.act_state == kabi.FLY_STATE)):
            kabi.direction_up_state = True
        elif((event.type, event.key) == (SDL_KEYUP, SDLK_UP) and (kabi.act_state == kabi.FLY_STATE)):
            kabi.direction_up_state = False
        elif((event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN) and (kabi.act_state == kabi.FLY_STATE)):
            kabi.direction_down_state = True
        elif((event.type, event.key) == (SDL_KEYUP, SDLK_DOWN) and (kabi.act_state == kabi.FLY_STATE)):
            kabi.direction_down_state = False

def enter():
    global kabi
    global background
    global cloud
    kabi = Kabi()
    background = BackGround()
    cloud = Cloud()

def exit():
    global kabi
    global background
    global cloud
    del(kabi)
    del(background)
    del(cloud)

def update():
    background.update()
    kabi.update()
    delay(0.1)

def draw():
    clear_canvas()
    background.draw()
    cloud.draw()
    kabi.draw()
    update_canvas()

