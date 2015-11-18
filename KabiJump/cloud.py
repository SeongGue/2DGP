import random

from pico2d import *

class Cloud:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 5.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    image = None

    CLOUD_ROW, CLOUD_COL = 120, 70
    def __init__(self):
        self.cloud_speed = 0
        self.x, self.y = random.randint(200, 730), random.randint(100, 600)
        if Cloud.image == None:
            Cloud.image = load_image('resource\\cloud_one.png')

    def update(self, frame_time):
        self.cloud_speed = Cloud.SCROLL_SPEED_PPS
        self.y -= self.cloud_speed * frame_time
        if(self.y < 0):
            self.x, self.y = random.randint(200, 730), random.randint(700, 1200)

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - Cloud.CLOUD_ROW / 2, self.y - Cloud.CLOUD_COL / 2 , self.x + Cloud.CLOUD_ROW / 2, self.y