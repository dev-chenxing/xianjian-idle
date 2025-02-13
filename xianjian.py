import os
import sys
from core import common
from core.ansi import color_cat, color_print as print
from core.cmds import parse_cmds
from core.game import Game
from core.utils import input_to

from pymitter import EventEmitter
event = EventEmitter()

path = "saves"
saves_list = None


def initialize():
	color_cat("./doc/welcome")
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
	game.load()
	common.game = game
	# game.start()
	game.position_room(game.李逍遥, "余杭客栈·李逍遥房")
	print("\n$green$欢迎您进入仙剑奇侠传，今后请使用 $brightyellow$帮助 $green$命令获得指令帮助。$normal$\n")
	color_cat("./doc/help")
	while True:
		input_to(parse_cmds)

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
		sys.exit() # When Ctrl-C is pressed, end the program.
