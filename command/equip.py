from core.ansi import color_print as print
from core.game import Game
import core.logging as log

pattern = "^装备(.*)"


def callback(arg: str):
	from core.common import game
	game: Game
	李逍遥 = game.李逍遥
	if arg:
		item = game.get_object(arg)
		if item:
			if game.get_item_count(李逍遥, item) > 0:
				game.remove_item(李逍遥, item)
				game.equip(李逍遥, item)
				print(f"{李逍遥.name}装备了{item.name}")
	else:
		print(f"$brightyellow${李逍遥.name}\n")
		for slot, equipment in 李逍遥.装备.items():
			print(f"$yellow${slot}$normal$  {equipment.name}")
