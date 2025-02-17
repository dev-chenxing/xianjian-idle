pattern = "^环顾四周$"

def callback():
	from core.common import game
	room = game.李逍遥.room
	room.describe()
