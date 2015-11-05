from pico2d import *
import random
import game_framework
import title_state

kabi = None
background = None
cloud = None
cloud_num = None

class Cloud:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint(0, 600)
        if Cloud.image == None:
            Cloud.image = load_image('resource\\cloud_one.png')
    def draw(self):
        self.image.draw(self.x, self.y)

class BackGround:
    global kabi
    def __init__(self):
        self.background_one = load_image('resource\\background_one.png')
        self.background_two = load_image('resource\\background_two.png')
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
    LEFT, RIGHT, UP, DOWN, STOP = 0, 1, 2, 3, 4

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
        self.direction_state = self.STOP
        self.act_state = self.STAND_STATE
        self.left_stand = load_image('resource\\Lidle_kabi.png')
        self.right_stand = load_image('resource\\Ridle_kabi.png')
        self.left_walk = load_image('resource\\Lwalk_kabi.png')
        self.right_walk = load_image('resource\\Rwalk_kabi.png')
        self.left_jump = load_image('resource\\Ljump_kabi.png')
        self.right_jump = load_image('resource\\Rjump_kabi.png')
        self.left_Fly = load_image('resource\\Lfly_kabi.png')
        self.right_Fly = load_image('resource\\Rfly_kabi.png')

        self.walk_frame = 0
        self.jump_frame = 0
        self.fly_frame = 0

        self.x, self.y = 400, 90

    # handle_state = {
    #     STAND_STATE : handle_stand,
    #     WALK_STATE : handle_walk,
    #     JUMP_STATE : handle_jump,
    #     FLY_STATE : handle_fly,
    #     FALL_STATE : handle_fall
    # }

    def handle_event(self, event):
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.direction_state = self.LEFT
            if self.act_state in (self.STAND_STATE, self.WALK_STATE):
                kabi.act_state = kabi.WALK_STATE

        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.direction_state = self.RIGHT
            if self.act_state in (self.STAND_STATE, self.WALK_STATE):
                kabi.act_state = kabi.WALK_STATE

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if(self.direction_state == self.LEFT):
                self.direction_state = self.STOP
                self.act_state = self.STAND_STATE

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if(self.direction_state == self.RIGHT):
                self.direction_state = self.STOP
                self.act_state = self.STAND_STATE

        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.act_state in (self.JUMP_STATE, self.FALL_STATE):
                kabi.act_state = kabi.FLY_STATE

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_SPACE):
            if self.act_state == self.FLY_STATE:
                self.act_state = kabi.FALL_STATE

        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE): ##비행 위에 쓰면 점프 안됨
            self.act_state = self.JUMP_STATE

        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.act_state == self.FLY_STATE:
                self.direction_state = self.UP

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            if self.direction_state == self.UP:
                self.direction_state = self.STOP

        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.act_state == self.FLY_STATE:
                self.direction_state = self.DOWN

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.direction_state == self.DOWN:
                self.direction_state = self.STOP

    def update(self):
        self.walk_frame = frame = (self.walk_frame + 1) % 10
        self.jump_frame = (self.jump_frame + 1) % 8
        self.fly_frame = (self.fly_frame + 1) % 7

        if(self.direction_state == self.LEFT):
            if(self.x > 0):
                self.x -= 10
        elif(self.direction_state == self.RIGHT):
            if(self.x < 800):
                self.x += 10

        #self.handle_state[self.act_state](self)

    def draw(self):
        if(self.direction_state == self.LEFT):
            if(self.act_state == self.STAND_STATE):
                self.left_stand.draw(self.x, self.y)
            elif(self.act_state == self.WALK_STATE):
                self.left_walk.clip_draw((self.walk_frame + 1) * 51, 0, 51, 50, self.x, self.y)
            elif(self.act_state == self.JUMP_STATE):
                self.left_jump.clip_draw(self.jump_frame * 50, 0, 40, 50, self.x, self.y)
            elif(self.act_state == self.FLY_STATE):
                self.left_Fly.clip_draw(self.fly_frame * 55, 0, 55, 50, self.x, self.y)
            elif(self.act_state == self.FALL_STATE):
                self.left_walk.clip_draw(0, 0, 51, 50, self.x, self.y)

        elif(self.direction_state == self.RIGHT):
            if(self.act_state == self.STAND_STATE):
                self.right_stand.draw(self.x, self.y)
            elif(self.act_state == self.WALK_STATE):
                self.right_walk.clip_draw(self.walk_frame * 51, 0, 51, 50, self.x, self.y)
            elif(self.act_state == self.JUMP_STATE):
                self.right_jump.clip_draw(self.jump_frame * 48, 0, 40, 50, self.x, self.y)
            elif(self.act_state == self.FLY_STATE):
                self.right_Fly.clip_draw(self.fly_frame * 55, 0, 55, 50, self.x, self.y)
            elif(self.act_state == self.FALL_STATE):
                self.right_walk.clip_draw(512, 0, 51, 50, self.x, self.y)

def handle_events():
    global kabi
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        else:
            kabi.handle_event(event)

def enter():
    global kabi
    global background
    global cloud_num
    kabi = Kabi()
    background = BackGround()
    cloud_num = [Cloud() for i in range(10)]

def exit():
    global kabi
    global background
    del(kabi)
    del(background)
    for cloud in cloud_num:
        del(cloud)

def update():
    background.update()
    kabi.update()
    delay(0.1)

def draw():
    clear_canvas()
    background.draw()
    for cloud in cloud_num:
        cloud.draw()
    kabi.draw()
    update_canvas()

