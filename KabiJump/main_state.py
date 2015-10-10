from pico2d import*
import game_framework
import title_state

class Kabi:
    def __init__(self):
        self.Rwalk = load_image('Rwalk_kabi.png')
        self.Lwalk = load_image('Lwalk_kabi.png')
        self.Ridle = load_image('Ridle_kabi.png')
        self.Lidle = load_image('Lidle_kabi.png')
        self.frame = 0;
        self.x, self.y = 400, 90
        self.RidleFlag, self.LidleFlag = True, False
        self.RwalkFlag, self.LwalkFlag = False, False

    def update(self):
        self.frame = (self.frame + 1) % 10
        if(self.RwalkFlag == True):
            self.x += 10
        elif(self.LwalkFlag == True):
            self.x -= 10
        delay(0.1)
    def draw(self):
        if(self.RidleFlag == True and self.LwalkFlag == False):
            self.Ridle.draw(self.x, self.y)
        elif(self.LidleFlag == True and self.RwalkFlag == False):
            self.Lidle.draw(self.x, self.y)
        elif(self.RwalkFlag == True):
            self.Rwalk.clip_draw(self.frame * 51, 0, 51, 51, self.x, self.y)
        elif(self.LwalkFlag == True):
            self.Lwalk.clip_draw((self.frame + 1) * 51, 0, 51, 51, self.x, self.y)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)

        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            kabi.RidleFlag = False
            kabi.LidleFlag = False
            kabi.RwalkFlag = False
            kabi.LwalkFlag = True
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            kabi.RidleFlag = False
            kabi.LidleFlag = True
            kabi.RwalkFalg = False
            kabi.LwalkFlag = False
        elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            kabi.RidleFlag = False
            kabi.LidleFlag = False
            kabi.RwalkFlag = True
            kabi.LwalkFlag = False
        elif(event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            kabi.RidleFlag = True
            kabi.LidleFlag = False
            kabi.RwalkFlag = False
            kabi.LwalkFalg = False

kabi = None

def enter():
    global kabi
    kabi = Kabi()
def exit():
    global kabi
    del(kabi)
def update():
    kabi.update()
def draw():
    clear_canvas()
    kabi.draw()
    update_canvas()

