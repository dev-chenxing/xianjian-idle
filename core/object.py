class Object:
	def __init__(self, game, object_type, name: str):
		self.object_type = object_type
		self.name = name
		if name not in game.objects:
			game.objects[name] = self
		else:
			raise ValueError("Already has an object with the name "+name)
