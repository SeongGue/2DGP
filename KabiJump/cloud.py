import random

from pico2d import *

class Cloud:

    image = None

    CLOUD_ROW, CLOUD_COL = 120, 70
    def __init__(self):
        # self.cloud_speed = 0
        # self.x, self.y = random.randint(200, 730), random.randint(100, 600)
        # self.high = self.y
        # if Cloud.image == None:
        #     Cloud.image = load_image('resource\\cloud_one.png')
        pass

    def update(self, frame_time):
        # self.cloud_speed = Cloud.SCROLL_SPEED_PPS
        # self.y -= self.cloud_speed * frame_time
        # if(self.y < 0):
        #     self.x, self.y = random.randint(200, 730), random.randint(700, 1200)
        pass

    def draw(self, scroll_high):
        # self.high = self.y - scroll_high
        # self.image.draw(self.x, self.high)
        pass

    def draw_bb(self):
        #draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        #return self.x - Cloud.CLOUD_ROW / 2, self.high - Cloud.CLOUD_COL / 2 , self.x + Cloud.CLOUD_ROW / 2, self.high
        pass