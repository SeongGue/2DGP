import random

from pico2d import *

class BigBall():
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    FALL_SPEED_KMPH = 20.0                    # Km / Hour
    FALL_SPEED_MPM = (FALL_SPEED_KMPH * 1000.0 / 60.0)
    FALL_SPEED_MPS = (FALL_SPEED_MPM / 60.0)
    FALL_SPEED_PPS = (FALL_SPEED_MPS * PIXEL_PER_METER)


    image = None
    def __init__(self):
        self.x, self.y = random.randint(100, 700), random.randint(600, 1200)
        self.fall_speed = random.randint(0, 20)
        if BigBall.image == None:
            #BigBall.image = load_image('resource\\image\\ball41x41.png')
            BigBall.image = load_image('resource\\image\\iceball.png')


    def stop(self):
        self.fall_speed = 0

    def update  (self, frame_time):
        self.fall_speed += BigBall.FALL_SPEED_PPS * frame_time
        self.y -= self.fall_speed * frame_time
        if (self.y < 0):
            self.x, self.y = random.randint(100, 700), random.randint(600, 1200)
            self.fall_speed = random.randint(0, 20)


    def draw(self):
        self.image.draw(self.x, self.y)


    def draw_bb(self):
       draw_rectangle(*self.get_bb())


    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def regen(self):
        self.x, self.y = random.randint(100, 700), random.randint(600, 1200)
        self.fall_speed = random.randint(0, 20)

