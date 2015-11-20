from pico2d import *

class Kabi:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 1.0
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    WALK_FRAMES_PER_ACTION = 10
    JUMP_FRAMES_PER_ACTION = 8
    FLY_FRAMES_PER_ACTION = 7

    JUMP_SPEED_KMPH = 40.0
    JUMP_SPEED_MPM = (JUMP_SPEED_KMPH * 1000.0 / 60.0)
    JUMP_SPEED_MPS = (JUMP_SPEED_MPM / 60.0)
    JUMP_SPEED_PPS = (JUMP_SPEED_MPS * PIXEL_PER_METER)

    GRAVITY_SPEED_KMPH = 100.0
    GRAVITY_SPEED_MPM = (GRAVITY_SPEED_KMPH * 1000.0 / 60.0)
    GRAVITY_SPEED_MPS = (GRAVITY_SPEED_MPM / 60.0)
    GRAVITY_SPEED_PPS = (GRAVITY_SPEED_MPS * PIXEL_PER_METER)

    FALL_SPEED_KMPH = 0
    FALL_SPEED_MPM = (FALL_SPEED_KMPH * 1000.0 / 60.0)
    FALL_SPEED_MPS = (FALL_SPEED_MPM / 60.0)
    FALL_SPEED_PPS = (FALL_SPEED_MPS * PIXEL_PER_METER)

    STAND_STATE, WALK_STATE, JUMP_STATE, FLY_STATE, FALL_STATE  = 0, 1, 2, 3, 4
    LEFT, STOP, RIGHT = -1, 0, 1
    DOWN, STOP ,UP= -1, 0, 1
    START_Y = 30

    KABI_BOX = 15

    def handle_stand(self, frame_time):
        if self.y != Kabi.START_Y:
            self.act_state = Kabi.FALL_STATE
        self.jump_power = Kabi.JUMP_SPEED_PPS
        self.gravity = Kabi.GRAVITY_SPEED_PPS
        self.fall_speed = Kabi.FALL_SPEED_PPS
        self.up_down_state = Kabi.DOWN

    def handle_walk(self, frame_time):
        if self.y != Kabi.START_Y:
            self.act_state = Kabi.FALL_STATE
        self.jump_power = Kabi.JUMP_SPEED_PPS
        self.gravity = Kabi.GRAVITY_SPEED_PPS
        self.fall_speed = Kabi.FALL_SPEED_PPS
        self.up_down_state = Kabi.DOWN

    def handle_jump(self, frame_time):
        self.y += self.jump_power * frame_time
        if(self.y > self.START_Y):
            self.jump_power -= self.gravity * frame_time
            if(self.jump_power < 0):
                self.up_down_state = Kabi.DOWN

        elif(self.y < self.START_Y):
            self.jump_power = Kabi.JUMP_SPEED_PPS
            self.y = self.START_Y
            self.act_state = Kabi. STAND_STATE
            if self.direction_state in (self.LEFT, self.RIGHT):
                self.act_state = Kabi.WALK_STATE

    def handle_fly(self, frame_time):
        self.fall_speed = Kabi.FALL_SPEED_PPS
        self.jump_power = Kabi.JUMP_SPEED_PPS
        self.gravity = Kabi.GRAVITY_SPEED_PPS
        distance = Kabi.RUN_SPEED_PPS * frame_time

        self.y += (self.up_down_state * distance)


    def handle_fall(self, frame_time):
        self.y -= self.fall_speed * frame_time

        if(self.y > self.START_Y):
                self.fall_speed += Kabi.GRAVITY_SPEED_PPS * frame_time

        elif(self.y < self.START_Y):
            self.fall_speed = Kabi.FALL_SPEED_PPS
            self.y = Kabi.START_Y
            self.act_state = Kabi.STAND_STATE
            if self.direction_state in (self.LEFT, self.RIGHT):
                self.act_state = Kabi.WALK_STATE

    def __init__(self):
        self.save_direction = Kabi.LEFT
        self.direction_state = Kabi.STOP
        self.up_down_state = Kabi.STOP
        self.act_state = Kabi.STAND_STATE
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

        self.walk_total_frames = 0.0
        self.jump_total_frames = 0.0
        self.fly_total_frames = 0.0

        self.x, self.y = 400, self.START_Y
        self.jump_power = Kabi.JUMP_SPEED_PPS
        self.gravity = Kabi.GRAVITY_SPEED_PPS
        self.fall_speed = Kabi.FALL_SPEED_PPS

    handle_state = {
        STAND_STATE : handle_stand,
        WALK_STATE : handle_walk,
        JUMP_STATE : handle_jump,
        FLY_STATE : handle_fly,
        FALL_STATE : handle_fall
    }

    def handle_event(self, event):
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.save_direction = Kabi.LEFT
            self.direction_state = Kabi.LEFT
            if self.act_state in (Kabi.STAND_STATE, Kabi.WALK_STATE):
                self.act_state = Kabi.WALK_STATE

        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.save_direction = Kabi.RIGHT
            self.direction_state = Kabi.RIGHT
            if self.act_state in (Kabi.STAND_STATE, Kabi.WALK_STATE):
                self.act_state = Kabi.WALK_STATE

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if(self.direction_state == Kabi.LEFT):
                self.direction_state = Kabi.STOP
                if self.act_state == Kabi.WALK_STATE:
                    self.act_state = Kabi.STAND_STATE

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if(self.direction_state == Kabi.RIGHT):
                self.direction_state = Kabi.STOP
                if self.act_state == Kabi.WALK_STATE:
                    self.act_state = Kabi.STAND_STATE

        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.act_state in (Kabi.JUMP_STATE, Kabi.FALL_STATE):
                self.act_state = Kabi.FLY_STATE
                self.up_down_state = Kabi.STOP
            else:
                self.act_state = Kabi.JUMP_STATE
                self.up_down_state = Kabi.STOP

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_SPACE):
            if self.act_state == Kabi.FLY_STATE:
                self.act_state = Kabi.FALL_STATE
                self.up_down_state = Kabi.DOWN

        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if self.act_state == Kabi.FLY_STATE:
                self.up_down_state = Kabi.UP

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            if (self.up_down_state, self.act_state) == (Kabi.UP, Kabi.FLY_STATE):
                self.up_down_state = Kabi.STOP

        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.act_state == Kabi.FLY_STATE:
                self.up_down_state = Kabi.DOWN

        elif(event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if (self.up_down_state, self.act_state) == (Kabi.DOWN, Kabi.FLY_STATE): #업 다운으로만 조건을 주면 구름에서 다운 방향키 뗄데 추락함
                self.up_down_state = Kabi.STOP

    def update(self, frame_time, scroll_high):
        def clamp(minimum, x, maximum):
            return max(minimum, min(x, maximum))

        distance = Kabi.RUN_SPEED_PPS * frame_time

        self.walk_total_frames += Kabi.WALK_FRAMES_PER_ACTION * Kabi.ACTION_PER_TIME * frame_time
        self.jump_total_frames += Kabi.JUMP_FRAMES_PER_ACTION * Kabi.ACTION_PER_TIME * frame_time
        self.fly_total_frames += Kabi.FLY_FRAMES_PER_ACTION * Kabi.ACTION_PER_TIME * frame_time

        self.walk_frame = int(self.walk_total_frames) % 10
        self.jump_frame = int(self.jump_total_frames) % 8
        self.fly_frame = int(self.fly_total_frames) % 7

        self.x += (self.direction_state * distance)

        self.x = clamp(0, self.x, 800)
        self.y -= scroll_high * frame_time

        self.handle_state[self.act_state](self, frame_time)

    def draw(self):
        if(self.save_direction == self.LEFT):
            if(self.act_state == Kabi.STAND_STATE):
                self.left_stand.draw(self.x, self.y)
            elif(self.act_state == Kabi.WALK_STATE):
                self.left_walk.clip_draw((self.walk_frame + 1) * 51, 0, 51, 50, self.x, self.y)
            elif(self.act_state == Kabi.JUMP_STATE):
                self.left_jump.clip_draw(self.jump_frame * 50, 0, 40, 50, self.x, self.y)
            elif(self.act_state == Kabi.FLY_STATE):
                self.left_Fly.clip_draw(self.fly_frame * 55, 0, 55, 50, self.x, self.y)
            elif(self.act_state == Kabi.FALL_STATE):
                self.left_walk.clip_draw(0, 0, 51, 50, self.x, self.y)

        elif(self.save_direction == self.RIGHT):
            if(self.act_state == Kabi.STAND_STATE):
                self.right_stand.draw(self.x, self.y)
            elif(self.act_state == Kabi.WALK_STATE):
                self.right_walk.clip_draw(self.walk_frame * 51, 0, 51, 50, self.x, self.y)
            elif(self.act_state == Kabi.JUMP_STATE):
                self.right_jump.clip_draw(self.jump_frame * 48, 0, 40, 50, self.x, self.y)
            elif(self.act_state == Kabi.FLY_STATE):
                self.right_Fly.clip_draw(self.fly_frame * 55, 0, 55, 50, self.x, self.y)
            elif(self.act_state == Kabi.FALL_STATE):
                self.right_walk.clip_draw(512, 0, 51, 50, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - Kabi.KABI_BOX, self.y - Kabi.KABI_BOX, self.x + Kabi.KABI_BOX, self.y + Kabi.KABI_BOX
    def stop(self):
        self.act_state = Kabi.STAND_STATE
        if self.direction_state in (self.LEFT, self.RIGHT):
            self.act_state = Kabi.WALK_STATE
    def death(self):
        pass
