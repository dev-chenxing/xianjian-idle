from core.object import Object


class Talisman(Object):
    def __init__(self, game, name: str):
        super().__init__(game, object_type="talisman", name=name)
