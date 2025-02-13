from core.ansi import fg, reset, color_print as print
from core.object import Object
from core.say import press_any_key_to_continue

class Character(Object):
	def __init__(self, game, name:str):
		super().__init__(game, name)
		self.经验值 = 0
		self.修行 = 1
		self.当前体力 = 150
		self.体力 = 150
		self.当前真气 = 100
		self.真气 = 100
		self.武术 = 35
		self.灵力 = 20
		self.防御 = 41
		self.身法 = 31
		self.吉运 = 32
		
	def say(self, text:str):
		print(fg.cyan+self.name+"："+reset+text)
		press_any_key_to_continue()
