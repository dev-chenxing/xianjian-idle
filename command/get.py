from core.game import Game

pattern = "^拿(.*)"


def callback(arg: str):
	from core.common import game
	game: Game
	李逍遥 = game.李逍遥
	item = game.get_object(arg)
	if item:
		room = 李逍遥.room
		for item_stack in room.items:
			if item_stack.object == item:
				if item_stack.count == 1:
					room.items.remove(item_stack)
					del item_stack
				else:
					item_stack.count -= 1
				game.add_item(李逍遥, item)
				return
