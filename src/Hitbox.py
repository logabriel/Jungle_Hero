from typing import TypeVar

from src import mixins

class Hitbox(mixins.CollidableMixin):
    def __init__(self, x: float, y: float, width: float, height: float) -> None: # type: ignore
        self.x = x
        self.y = y
        self.width = width
        self.height = height

