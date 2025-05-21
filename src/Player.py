"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Player.
"""

from typing import TypeVar

from gale.input_handler import InputData

from src.GameEntity import GameEntity
from src.states.entities import player_states
from src.GameItem import GameItem

import settings

class Player(GameEntity):
    girl_save = 0
    girl_save_total = 0
    def __init__(self, x: int, y: int, player_type: int, game_level: TypeVar("GameLevel")) -> None: # type: ignore
        if player_type == 1:
            super().__init__(
                x,
                y,
                22,
                42,
                "robber", 
                game_level,
                sound="hit_bowie",
                states={
                    "idle": lambda sm: player_states.IdleState(self, sm),
                    "walk": lambda sm: player_states.WalkState(self, sm),
                    "jump": lambda sm: player_states.JumpState(self, sm),
                    "fall": lambda sm: player_states.FallState(self, sm),
                    "dead": lambda sm: player_states.DeadState(self, sm),
                    "attack": lambda sm: player_states.AttackState(self, sm),
                },
                animation_defs={
                    "idle": {"frames": [0, 1, 2], "interval": 0.15},
                    "walk": {"frames": [4, 5, 6, 7, 8, 9], "interval": 0.15},
                    "jump": {"frames": [10, 11, 12, 13, 14, 15], "interval": 0.15},
                    "attack": {"frames": [17, 18, 19, 20, 21], "interval": 0.15}
                },
            )
        else:
            super().__init__(
                x,
                y,
                22,
                37,
                "steamMan",
                game_level,
                sound="hit_bowie",
                states={
                    "idle": lambda sm: player_states.IdleState(self, sm),
                    "walk": lambda sm: player_states.WalkState(self, sm),
                    "jump": lambda sm: player_states.JumpState(self, sm),
                    "fall": lambda sm: player_states.FallState(self, sm),
                    "dead": lambda sm: player_states.DeadState(self, sm),
                    "attack": lambda sm: player_states.AttackState(self, sm),
                },
                animation_defs={
                    "idle": {"frames": [0, 1, 2, 3], "interval": 0.15},
                    "walk": {"frames": [4, 5, 6, 7, 8, 9], "interval": 0.15},
                    "jump": {"frames": [10, 11, 12, 13, 14, 15], "interval": 0.15},
                    "attack": {"frames": [16, 17, 18, 19, 20], "interval": 0.15}
                },
            )
        self.score = 0
        self.coins_counter = {54: 0, 55: 0, 61: 0, 62: 0}
        self.key = False
        self.player_type = player_type
        self.direcction = settings.RIGHT

    def on_input(self, input_id: str, input_data: InputData) -> None:
        self.state_machine.on_input(input_id, input_data)
    
    def collision_on_top(self) -> bool:
        collision_rect = self.get_collision_rect()

        # Row for the center of the player
        i = self.tilemap.to_i(collision_rect.centery)

        # Left and right columns
        left = self.tilemap.to_j(collision_rect.left)
        right = self.tilemap.to_j(collision_rect.right)

        if self.tilemap.collides_tile_on(
            i - 1, left, self, GameItem.BOTTOM
        ) or self.tilemap.collides_tile_on(i - 1, right, self, GameItem.BOTTOM):
            return True

        return False
