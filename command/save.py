from core.game import Game


pattern = "^储存进度$"

def callback():
	from core.common import game
	game: Game
	game.save_game()
