import random

from pico2d import *

class BigBall():
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


    image = None
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 500
        self.fall_speed = 0
        if BigBall.image == None:
            BigBall.image = load_image('resource\\ball41x41.png')

    def stop(self):
        self.fall_speed = 0

    def update(self, frame_time):
        self.y -= frame_time * self.fall_speed
        self.fall_speed += frame_time * BigBall.RUN_SPEED_PPS

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
       draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10
