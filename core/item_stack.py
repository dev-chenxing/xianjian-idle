class ItemStack:
	def __init__(self, object, count: int = 1):
		self.object = object
		self.count = count

	def __str__(self):
		return f"{self.count}{self.object.unit}{self.object.name}"
