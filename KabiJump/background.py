from pico2d import *


class Background:
    global Kabi

    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    SCROLL_SPEED_KMPH = 5.0                    # Km / Hour
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self, w, h):
        self.floor = load_image('resource\\grass.png')
        self.image = load_image('resource\\background.png') # 960x272

        self.speed_y = 0
        self.down = 0
        self.screen_width = w
        self.screen_height = h

    def update(self, frame_time):
        # self.speed_y = Background.SCROLL_SPEED_PPS
        # self.down = (self.down + frame_time * self.speed_y) % self.image.h
        pass

    def draw(self):

        y = int(self.down)

        h = min(self.screen_height, self.image.h - y)

        self.image.clip_draw_to_origin(0, y, self.screen_width, h, 0, 0)
        self.image.clip_draw_to_origin(0, 0, self.screen_width, self.screen_height, 0, h)

        self.floor.draw(400,0)

    def handle_event(self, event):
        pass


