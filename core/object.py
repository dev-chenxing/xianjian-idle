class Object:
	def __init__(self, game, object_type, name: str):
		if name in game.objects:
			raise ValueError("Already has an object with the name "+name)

		self.object_type = object_type
		self.name = name
		self.unit = "个"

		game.objects[name] = self

