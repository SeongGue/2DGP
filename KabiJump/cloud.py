import random

from pico2d import *

class Cloud:
    # bot_image = None
    # mid_imgae = None
    # top_image = None
    image = None

    CLOUD_ROW, CLOUD_COL = 120, 70
    def __init__(self):
        # self.bot_image_x, self.bot_image_y = random.randint(150, 300), random.randint(100, 200)
        # self.mid_image_x, self.mid_image_y = random.randint(450, 650), random.randint(300, 400)
        # self.top_image_x, self.top_image_y = random.randint(150, 300), random.randint(500, 600)

        self.x, self.y = random.randint(200, 730), random.randint(100, 600)
        # Cloud.bot_image = load_image('resource\\cloud_one.png')
        # Cloud.mid_image = load_image('resource\\cloud_one.png')
        # Cloud.top_image = load_image('resource\\cloud_one.png')
        if Cloud.image == None:
            Cloud.image = load_image('resource\\cloud_one.png')

    def draw(self):
        # self.bot_image.draw(self.bot_image_x, self.bot_image_y)
        # self.mid_image.draw(self.mid_image_x, self.mid_image_y)
        # self.top_image.draw(self.top_image_x, self.top_image_y)
        self.image.draw(self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - Cloud.CLOUD_ROW / 2, self.y - Cloud.CLOUD_COL / 2 , self.x + Cloud.CLOUD_ROW / 2, self.y