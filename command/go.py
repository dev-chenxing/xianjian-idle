from core.game import Game


pattern = "^[向往]?([东南西北上下])走?$"

directions = ["东", "南", "西", "北", "上", "下"]

def callback(arg: str):
	from core.common import game
	game: Game
	李逍遥 = game.李逍遥
	direction = arg
	if direction in 李逍遥.room.exits:
		# if 李逍遥.room.exit_blocked[direction]():
			game.position_room(李逍遥, 李逍遥.room.exits[direction])
