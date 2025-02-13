from core.object import Object

class Armor(Object):
	def __init__(self, game, name:str, slot):
		super().__init__(game, object_type="armor", name=name)
		self.slot = slot
