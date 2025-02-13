from core.object import Object


class Ingredient(Object):
    def __init__(self, game, name: str):
        super().__init__(game, object_type="ingredient", name=name)
