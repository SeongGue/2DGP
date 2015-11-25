from pico2d import *

PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
SCROLL_SPEED_KMPH = 20.0                    # Km / Hour
SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

class Background:
    global SCROLL_SPEED_PPS

    def __init__(self, w, h):
        self.image = load_image('resource\\background.png') # 960x272

        self.speed_y = 0
        self.down = 0
        self.screen_width = w
        self.screen_height = h

    def update(self, frame_time):
        self.speed_y =  SCROLL_SPEED_PPS
        self.down = (self.down + frame_time * self.speed_y) % self.image.h

    def draw(self):

        y = int(self.down)

        h = min(self.screen_height, self.image.h - y)

        self.image.clip_draw_to_origin(0, y, self.screen_width, h, 0, 0)
        self.image.clip_draw_to_origin(0, 0, self.screen_width, self.screen_height, 0, h)


class Grass:
    global SCROLL_SPEED_PPS

    def __init__(self, x, y):
        self.image = load_image('resource\\grass.png')
        self.x, self.y = x, y

    def change_field(self, frame_time):
        if self.y > 0:
            self.y -= SCROLL_SPEED_PPS * frame_time
        if self.y <= 0:
            self.y = 600

    def draw(self):
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - self.image.w / 2, self.y - self.image.h / 2, self.x + self.image.w / 2, self.y + self.image.h /3


