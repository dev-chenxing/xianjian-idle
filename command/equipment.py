from core.ansi import color_print as print

pattern = "装备"

def callback():
	from core.common import game
	李逍遥 = game.李逍遥
	print(f"$brightyellow${李逍遥.name}\n")
	for slot, equipment in 李逍遥.装备.items():
		print(f"$yellow${slot}$normal$  {equipment.name}")
