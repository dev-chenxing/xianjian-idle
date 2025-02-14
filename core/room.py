from core.ansi import color_print as print
from core.item_stack import ItemStack


class Room:
	def __init__(self, game, name: str, area: str | None):
		if name in game.rooms:
			raise ValueError("Already has a cell with the name "+name)

		self.area = area
		self.name = name
		self.full_name = f"{area}·{name}" if area else name
		self.characters = []
		self.items: list[ItemStack] = []
		self.exits: dict[str, Room] = {}

		game.rooms[self.full_name] = self

	def describe(self):
		print(f"\n$cyan$【{self.full_name}】")
		if self.items:
			for item_stack in self.items:
				print(f"  {str(item_stack)}")
