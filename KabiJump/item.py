from pico2d import *
import random

class Shield:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    FALL_SPEED_KMPH = 20.0                    # Km / Hour
    FALL_SPEED_MPM = (FALL_SPEED_KMPH * 1000.0 / 60.0)
    FALL_SPEED_MPS = (FALL_SPEED_MPM / 60.0)
    FALL_SPEED_PPS = (FALL_SPEED_MPS * PIXEL_PER_METER)

    image = None

    def __init__(self):
        if Shield.image == None:
            Shield.image = load_image('resource\\image\\helmet.png')
        self.x, self.y = random.randint(100, 700), 500
        self.fall_speed = 0

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self, frame_time):
        self.fall_speed += Shield.FALL_SPEED_PPS * frame_time
        #self.y -= self.fall_speed * frame_time

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - Shield.image.w / 2, self.y - Shield.image.h / 2, self.x + Shield.image.w / 2, self.y + Shield.image.h / 2


def test_item():
    open_canvas()
    shield = Shield()
    while shield.y > 0:
        clear_canvas()
        shield.draw()
        update_canvas()
        shield.update(0.0025)
    delay(1)
    close_canvas()

if __name__ == '__main__':
    test_item()