"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class DeadState for player.
"""

from src.states.entities.BaseEntityState import BaseEntityState
import settings

class DeadState(BaseEntityState):
    def enter(self) -> None:
        settings.SOUNDS["man_dead_2"].stop()
        settings.SOUNDS["man_dead_2"].play()
        self.entity.is_dead = True
