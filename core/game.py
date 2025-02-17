import importlib
import os
import pathlib
import time
import pickle

from core.ansi import color_print as print
from core.armor import Armor
from core.character import Character
from core.ingredient import Ingredient
from core.item_stack import ItemStack
import core.logging as log
from core.object import Object
from core.room import Room
from core.say import say
from core.talisman import Talisman
from core.weapon import Weapon


class Game:
	def __init__(self):
		self.start_time = time.time()
		self.rooms = {}
		self.objects = {}

	def add_item(self, character: Character, item: Object, message=True):
		added_item = False
		for item_stack in character.物品:
			if item_stack.object == item:
				item_stack.count += 1
				added_item = True
				break
		if not added_item:
			character.物品.append(ItemStack(object=item))
		if message:
			print(f"得到{item.name}")

	def equip(self, character: Character, item, add_item=True):
		log.debug(f"$blue$equip$normal$({character.name}, {item.name})")
		if item.object_type == "armor":
			equipment_slot = {"头": "头戴", "披": "披挂", "身": "身穿", "脚": "脚穿", "佩戴": "配带"}
			if item.slot in equipment_slot.keys():
				slot = equipment_slot[item.slot]
				slot_equipment = character.装备[slot]
				if slot_equipment:
					print(f"{self.李逍遥.name}换下{slot_equipment.name}")
					if add_item:
						log.debug(f"将{slot_equipment.name}加入物品栏")
						self.add_item(character, slot_equipment, message=False)
				character.装备[slot] = item
				log.debug(f"{item.name} is equipped")
		elif item.object_type == "weapon":
			character.装备["手持"] = item
			log.debug(f"{item.name} is equipped")

	def get_item_count(self, character: Character, item):
		for item_stack in character.物品:
			if item_stack.object == item:
				return item_stack.count
		return 0

	def get_object(self, name: str) -> Object | None:
		if name in self.objects:
			return self.objects[name]

	def get_room(self, name: str) -> Room | None:
		if name in self.rooms:
			return self.rooms[name]

	def load(self):
		self.load_items()
		self.load_characters()
		self.load_rooms()

	def load_characters(self):
		data_dir = "data"
		sub_dir = "character"
		full_dir = os.path.join(data_dir, sub_dir)
		log.debug(f"Loading {sub_dir}...")
		for file in os.listdir(full_dir):
			path = pathlib.Path(os.path.join(full_dir, file))
			if path.is_file():
				name = path.stem
				module = importlib.import_module(
					f"{data_dir}.{sub_dir}.{name}")
				if hasattr(module, "object_type") and module.object_type == "character":
					character = Character(self, name=module.name)
					if hasattr(module, "equipment") and module.equipment:
						for e in module.equipment:
							item = self.get_object(e["name"])
							if item:
								self.equip(character, item, add_item=True)
							else:
								log.error(
									f"Found invalid equipment {e.name} in {sub_dir} file {name}")
					if hasattr(module, "is_player") and module.is_player:
						self.李逍遥 = character
				else:
					log.error(f"Found invalid {sub_dir} file {name}")

	def load_items(self):
		data_dir = "data"
		sub_dir = "item"
		full_dir = os.path.join(data_dir, sub_dir)
		log.debug(f"Loading {sub_dir}...")
		for file in os.listdir(full_dir):
			path = pathlib.Path(os.path.join(full_dir, file))
			if path.is_file():
				name = path.stem
				module = importlib.import_module(
					f"{data_dir}.{sub_dir}.{name}")
				if hasattr(module, "object_type"):
					item = None
					if module.object_type == "armor":
						item = Armor(self, name=module.name,
							slot=module.slot)
					elif module.object_type == "weapon":
						item = Weapon(self, name=module.name)
					elif module.object_type == "talisman":
						item = Talisman(self, name=module.name)
					elif module.object_type == "ingredient":
						item = Ingredient(self, name=module.name)
					if item:
						item.unit = module.unit
						item.value = module.value
						if hasattr(module, "description"):
							item.description = module.description
				else:
					log.error(f"Found invalid {sub_dir} file {name}")

	def load_rooms(self):
		data_dir = "data"
		sub_dir = "room"
		full_dir = os.path.join(data_dir, sub_dir)
		log.debug(f"Loading {sub_dir}...")
		for file in os.listdir(full_dir):
			path = pathlib.Path(os.path.join(full_dir, file))
			if path.is_file():
				name = path.stem
				module = importlib.import_module(
					f"{data_dir}.{sub_dir}.{name}")
				if hasattr(module, "name"):
					if hasattr(module, "area"):
						room = Room(self, area=module.area, name=module.name)
					else:
						room = Room(self, name=module.name)
					if hasattr(module, "items") and module.items:
						for i in module.items:
							item = self.get_object(i["name"])
							if item:
								room.items.append(ItemStack(object=item))
							else:
								log.error(
									f"Found invalid item {i.name} in {sub_dir} file {name}")
					if hasattr(module, "characters") and module.characters:
						for c in module.characters:
							character: Character = self.get_object(c)
							if character:
								room.characters.append(character)
								character.room = room
							else:
								log.error(
									f"Found invalid character {c.name} in {sub_dir} file {name}")
					if hasattr(module, "exits") and module.exits:
						for direction, room_name in module.exits.items():
							room.exits[direction] = room_name
				else:
					log.error(f"Found invalid {sub_dir} file {name}")

	def position_room(self, character: Character, room_name: str):
		log.debug(f"position_room({character.name}), {room_name}")
		room = self.get_room(name=room_name)
		if room:
			leaving_room = character.room
			room.characters.append(character)
			character.room = room
			if character == self.李逍遥:
				room.describe()
			elif self.李逍遥.room == leaving_room:
				print(f"{character.name}离开了{leaving_room.name}")

	def remove_item(self, character: Character, item):
		for item_stack in character.物品:
			if item_stack.object == item:
				if item_stack.count == 1:
					character.物品.remove(item_stack)
					del item_stack
				else:
					item_stack.count -= 1

	def save_game(self, file:str="quicksave", name:str="Quicksave"):
		with open(f"{file}.dat", 'wb') as save_file:
			pickle.dump([name, self.李逍遥], save_file)

	def start(self):
		李逍遥: Character = self.李逍遥
		李大娘: Character = self.get_object("李大娘")

		print("\n$cyan$【余杭客栈·李逍遥房】$normal$\n")
		say("李～逍～遥，李～逍～遥！")
		李逍遥.say("哇哇！作恶多端的罗煞鬼婆！")
		李逍遥.say("既然落在你的手里，要杀要剐不用多说！")
		李大娘.say("李逍遥！你皮痒啊？敢说老娘是什么鬼婆！")
		李逍遥.say("哎呦～疼啊！")
		李大娘.say("又在作白日梦了！你也老大不小了，整天疯疯癫癫地，也不学学做正经事！")
		李逍遥.say("婶婶～你不要每次叫人起床都拿锅呀、铲呀，乱敲一通的，会吓死人哪！")
		李逍遥.say("咱们这木床又不牢靠，万一我给摔死了，咱们李家就绝后啦！")
		李大娘.say("不这样叫得醒你吗？好歹你也跟林师傅学过几个月的木工，床不牢自己动手修一修不就好了？")
		李大娘.say("就只会削些木刀木剑的，成天学你爹舞刀弄剑，没个定性，有哪家姑娘愿意嫁给你喔．．")
		李逍遥.say("那我爹怎么会娶到我娘？")
		李大娘.say("啧！你娘也是跟你爹一个样儿！嫁到咱们李家来，也不做针线女红，就只会跟着你爹疯．．")
		李逍遥.say("嘿．．大家都说～他们是江湖上人人羡慕的鸳鸯侠侣呢！")
		李大娘.say("是哦～侠侣？说要去行侠仗义，丢下你这惹祸精，一去无回。")
		李大娘.say("还不是我这老太婆省吃俭用的开了这么一家小小的客栈，才把你拉拔到这么大，结果养出这么一个懒鬼！")
		李逍遥.say("谁说我是懒鬼啦？")
		李逍遥.say("我将来要像我爹娘一样练成绝世武功，纵横四海、称霸江湖的一代大侠！")
		李大娘.say("少跟老娘鬼扯淡！")
		李大娘.say("你呀～游手好闲是出了名的，要不是这回我忙不过来，才不指望你这懒鬼来帮忙呢！")
		李逍遥.say("一大早就有客人上门啦？")
		李大娘.say("是啊．．还不快过来帮忙！")
		say("李大娘离开了李逍遥房。")
		李逍遥.say("真没意思．．一大清早就要人家做这个又做那个的．．")
		李逍遥.say("嘿．．昨晚做好的密道正好派上用场，这次就从这里溜出去吧．．")
		李大娘.say("逍遥！还窝在房里干啥？快出来帮忙招呼客人！")
		李逍遥.say("喔！．．我马上就去！")
		李逍遥.say("啧～算了，晚上再用密道吧，现在被发现就惨了！")
