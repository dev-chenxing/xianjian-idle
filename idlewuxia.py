import os
import time
from ansi import color_cat, color_print as print
import sys
from utils import input_to

from pymitter import EventEmitter
event = EventEmitter()

path = "saves"
saves_list = None


class Game:
    start_time = time.time()


def initialize():
    color_cat("./help/welcome")
    get_saves_list()
    main_menu()


def get_saves_list():
    if os.path.exists(path) and os.path.isdir(path):
        global saves_list
        saves_list = os.listdir(path)


def main_menu():
    print("请选择：")
    print("$yellow$(新)$normal$的故事")
    print("$yellow$(旧)$normal$的回忆")
    input_to(new_game_or_load)


def new_game_or_load(param: str):
    if param == "新":
        new_game()
    elif param == "旧":
        if saves_list:
            for i, save in enumerate(saves_list):
                print((i+1)+") "+save)
            input_to(load)
        else:
            print("$red$没有找到旧的存档，请开始新的故事")
            main_menu()
    else:
        main_menu()


def new_game():
    game = Game()


def load(param: str):
    load_save(saves_list[int(param)-1])


def load_save(file: str):
    print("\n$red$✖$normal$ has not been implemented")

    # If this program was run (instead of imported), run the game:
if __name__ == '__main__':
    try:
        initialize()
        event.emit("initialized")
        print("全文完")
    except KeyboardInterrupt:
        print("\n$red$✖$normal$ 退出游戏")
        sys.exit()  # When Ctrl-C is pressed, end the program.
