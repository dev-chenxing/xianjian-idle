from digit2chinese import digit2chinese

from core.object import Object


class ItemStack:
    def __init__(self, object, count: int = 1):
        self.object: Object = object
        self.count = count

    def __str__(self):
        return f"{digit2chinese(self.count, style=1)}{self.object.unit}{self.object.name}"
