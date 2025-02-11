from core.ansi import fg, reset, color_print as print
from core.object import Object
from core.say import press_any_key_to_continue

class Character(Object):
	def __init__(self, game, name:str):
		super().__init__(game, name)
	def say(self, text:str):
		print(fg.cyan+self.name+"："+reset+text)
		press_any_key_to_continue()
