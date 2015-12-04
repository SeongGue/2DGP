from pico2d import *


class Ui():
    def __init__(self):
        self.font = load_font('resource\\font\\ConsolaMalgun.ttf', 20)
        self.gauge_bar = load_image('resource\\image\\gauge_bar.png')
        self.gauge_bar_background = load_image('resource\\image\\gauge_bar_background.png')
        self.score = 0
        self.time = 0
        self.gh = self.gauge_bar.h

    def draw_font(self):
        self.font.draw(30, 60, 'HIGH %.1f M' % (self.score/100))
        self.font.draw(30, 40, 'time %.1f' % self.time)

    def draw_gauge_bar(self, kabi_x, kabi_y, fly_gauge):
        gauge_len = self.gh - fly_gauge * 0.3
        self.gauge_bar_background.draw(kabi_x + 25, kabi_y, self.gauge_bar_background.w, self.gauge_bar_background.h)
        self.gauge_bar.draw(kabi_x + 25, kabi_y - gauge_len / 2, self.gauge_bar.w, self.gh - gauge_len)

    def update(self, frame_time, kabi_y, save_time):
        self.time = get_time()
        self.time -= save_time
        self.score = kabi_y


def  test_ui():
    open_canvas()
    ui = Ui()
    #open_canvas()
    for i in range(100):
        ui.score = i
        ui.update(0,1)
        clear_canvas()
        ui.draw_font()
        update_canvas()
    delay(3)
    close_canvas()

if __name__ == '__main__':#(7)
    test_ui()