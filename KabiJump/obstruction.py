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
        self.x, self.y = random.randint(10, 790), random.randint(600, 1200)
        self.fall_speed = random.randint(0, 20)
        if BigBall.image == None:
            BigBall.image = load_image('resource\\image\\iceball.png')


    def stop(self,shield):
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


class UFO:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    FALL_SPEED_KMPH = 20.0                    # Km / Hour
    FALL_SPEED_MPM = (FALL_SPEED_KMPH * 1000.0 / 60.0)
    FALL_SPEED_MPS = (FALL_SPEED_MPM / 60.0)
    FALL_SPEED_PPS = (FALL_SPEED_MPS * PIXEL_PER_METER)

    image = None

    UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT = 0, 1, 2, 3

    def __init__(self):
        self.x, self.y = random.randint(500, 700), random.randint(300, 500)

        self.speed = UFO.FALL_SPEED_PPS
        if UFO.image == None:
            UFO.image = load_image('resource\\image\\ufo.png')
        self.direction = random.randint(0,3)


    def update  (self, frame_time):
        self.change_direction()
        if self.y == -30:
            self.y = random.randint(300, 500)

        if self.direction == UFO.UP_RIGHT:
            self.x += self.speed * frame_time
            self.y += self.speed * frame_time
        elif self.direction == UFO.UP_LEFT:
            self.x -= self.speed * frame_time
            self.y += self.speed * frame_time
        elif self.direction == UFO.DOWN_RIGHT:
            self.x += self.speed * frame_time
            self.y -= self.speed * frame_time
        elif self.direction == UFO.DOWN_LEFT:
            self.x -= self.speed * frame_time
            self.y -= self.speed * frame_time




    def draw(self):
        UFO.image.draw(self.x, self.y)


    def draw_bb(self):
       draw_rectangle(*self.get_bb())


    def get_bb(self):
        return self.x - UFO.image.w / 2, self.y - UFO.image.h / 2, self.x + UFO.image.w / 2, self.y + UFO.image.h / 2

    def change_direction(self):
        if self.x > 775:
            self.x = 775
            if self.direction == UFO.UP_RIGHT:
                self.direction = UFO.UP_LEFT
            elif self.direction == UFO.DOWN_RIGHT:
                self.direction = UFO.DOWN_LEFT
        elif self.x < 25:
            self.x = 25
            if self.direction == UFO.UP_LEFT:
                self.direction = UFO.UP_RIGHT
            elif self.direction == UFO.DOWN_LEFT:
                self.direction = UFO.DOWN_RIGHT
        elif self.y > 575:
            self.y = 575
            if self.direction == UFO.UP_RIGHT:
                self.direction = UFO.DOWN_RIGHT
            elif self.direction == UFO.UP_LEFT:
                self.direction = UFO.DOWN_LEFT
        elif self.y < 25:
            self.y = 25
            if self.direction == UFO.DOWN_RIGHT:
                self.direction = UFO.UP_RIGHT
            elif self.direction == UFO.DOWN_LEFT:
                self.direction = UFO.UP_LEFT
