import random

from pico2d import *

class Cloud:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 30.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    image = None
    collision = None
    PRE_COL, AFT_COL = 0, 1

    def __init__(self, y):
        self.x, self.y = random.randint(200, 730), y + random.randint(100, 500)
        self.cloud_state = Cloud.PRE_COL
        if Cloud.image == None:
            Cloud.image = load_image('resource\\cloud.png')
        if Cloud.collision == None:
            Cloud.collision = load_image('resource\\collision_cloud.png')


    def update(self, frame_time, change_field):
        self.cloud_speed = Cloud.SCROLL_SPEED_PPS
        self.y -= self.cloud_speed * frame_time
        if(self.y <= 0):
            self.x, self.y = random.randint(200, 730), random.randint(1300, 1700)

    def draw(self):
        if self.cloud_state == Cloud.PRE_COL:
            self.image.draw(self.x, self.y)

        elif self.cloud_state == Cloud.AFT_COL:
            self.collision.draw(self.x, self.y)


    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def get_bb(self):
        return self.x - Cloud.image.w / 2, self.y - Cloud.image.h / 2 , self.x + Cloud.image.w / 2, self.y

    def change_cloud(self):
        self.cloud_state = Cloud.AFT_COL

