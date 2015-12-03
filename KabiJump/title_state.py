import game_framework
import main_state
from pico2d import *


name = "TitleState"
image = None
sound =None

def enter():
    global image, sound
    image = load_image('resource\\image\\kabi_title.png')
    sound = load_music('resource\\sound\\background_Title.mp3')
    sound.set_volume(64)
    sound.repeat_play()


def exit():
    global image, sound
    del(image)
    del(sound)

def handle_events(frame_time):
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(main_state)

def draw(frame_time):
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass






