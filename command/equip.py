from core.ansi import color_print as print
from core.game import Game

pattern = "^装备(.*)"


def callback(arg: str):
	from core.common import game
	game: Game
	李逍遥 = game.李逍遥
	if arg:
		item = game.get_object(arg)
		if item:
			if item in 李逍遥.物品:
				李逍遥.物品.remove(item)
				game.equip(李逍遥, item)
	else:
		print(f"$brightyellow${李逍遥.name}\n")
		for slot, equipment in 李逍遥.装备.items():
			print(f"$yellow${slot}$normal$  {equipment.name}")
