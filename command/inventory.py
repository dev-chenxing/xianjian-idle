from core.ansi import color_print as print

pattern = "物品"

def callback():
	from core.common import game
	李逍遥 = game.李逍遥
	if 李逍遥.物品:
		pass
	else:
		print("目前李逍遥没有携带任何物品。")

