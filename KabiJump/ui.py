from pico2d import *


class Ui():
    def __init__(self):
        self.font = load_font('resource\\font\\ConsolaMalgun.ttf', 20)
        self.score = 0
        self.time = 0

    def draw(self):
        print('SCORE %d' % self.score)
        print('time %f' % get_time())
        self.font.draw(100, 100, 'SCORE %d, time %f' % (self.score, self.time), (255,255,255))

    def update(self, frame_time, kabi_y):
        self.score = kabi_y

def  test_ui():
    open_canvas()
    ui = Ui()
    #open_canvas()
    for i in range(100):
        ui.score = i
        ui.update(0,1)
        clear_canvas()
        ui.draw()
        update_canvas()
    delay(1)
    close_canvas()

if __name__ == '__main__':#(7)
    test_ui()