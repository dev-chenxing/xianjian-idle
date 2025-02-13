from core.object import Object

class Weapon(Object):
	def __init__(self, game, name:str):
		super().__init__(game, object_type="weapon",name=name)
