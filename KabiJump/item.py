from pico2d import *
import random

class Shield:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    FALL_SPEED_KMPH = 20.0                    # Km / Hour
    FALL_SPEED_MPM = (FALL_SPEED_KMPH * 1000.0 / 60.0)
    FALL_SPEED_MPS = (FALL_SPEED_MPM / 60.0)
    FALL_SPEED_PPS = (FALL_SPEED_MPS * PIXEL_PER_METER)

    big_h = None
    small_h1 = None
    small_h2 = None
    small_h3 = None


    def __init__(self):
        if Shield.big_h == None:
            self.big_h = load_image('resource\\image\\Big_helmet.png')
        if Shield.small_h1 == None:
            self.small_h1 = load_image('resource\\image\\small_helmet.png')
        if Shield.small_h2 == None:
            self.small_h2 = load_image('resource\\image\\small_helmet.png')
        if Shield.small_h3 == None:
            self.small_h3 = load_image('resource\\image\\small_helmet.png')
        self.x, self.y = random.randint(100, 700), 800
        self.fall_speed = 0
        self.shield_num = 0
        self.gen_time = 0

    def draw(self):
        self.big_h.draw(self.x, self.y)
        if self.shield_num > 0:
            self.small_h1.draw(5, 20, self.small_h1.w, self.small_h1.h)
        if self.shield_num > 1:
            self.small_h1.draw(25, 20, self.small_h2.w, self.small_h2.h)
        if self.shield_num > 2:
            self.small_h1.draw(45, 20, self.small_h3.w, self.small_h3.h)

    def update(self, frame_time):
        self.fall_speed += Shield.FALL_SPEED_PPS * frame_time
        self.y -= self.fall_speed * frame_time
        if self.y < -20:
            self.y = -30
        if self.y == -30:
            self.gen_time += 0.01
            if self.gen_time > 6.0 * (self. shield_num + 1):
                self.x, self.y = random.randint(100, 700), 800
                self.fall_speed = 0
                self.gen_time = 0
        print(self.shield_num)


    def eat_shield(self):
        self.y = -30
        if self.shield_num < 3:
            self.shield_num += 1

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - self.big_h.w / 2, self.y - self.big_h.h / 2, self.x + self.big_h.w / 2, self.y + self.big_h.h / 2


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