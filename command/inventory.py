from core.ansi import color_print as print
from core.game import Game
from core.utils import ljust

pattern = "^物品$"


def callback():
	from core.common import game
	game: Game
	李逍遥 = game.李逍遥
	if 李逍遥.物品:
		for item_stack in 李逍遥.物品:
			print(f"$yellow${ljust(str(item_stack), 12)}  $normal${item_stack.object.description or ""}")
	else:
		print("目前李逍遥没有携带任何物品。")
