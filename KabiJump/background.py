from pico2d import *
from kabi import Kabi


class Background:
    global Kabi
    def __init__(self):
        self.background_one = load_image('resource\\background_one.png')
        self.background_two = load_image('resource\\background_two.png')
        self.floor = load_image('resource\\grass.png')
        self.y1 = 536
        self.y2 = 1602

    def update(self):
        # if(Kabi.y >300 and Kabi.up_down_state == Kabi.UP):
        #     self.y1 -= 10
        #     self.y2 -= 10
        # if(self.y1 < -600):
        #     self.y1 = 1506
        # elif(self.y2 < -500):
        #     self.y2 = 1602
        pass

    def draw(self):
        self.background_one.draw(0, self.y1)
        self.background_two.draw(0, self.y2)
        self.floor.draw(400,0)
