"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class JumpState for player.
"""

from gale.input_handler import InputData

import settings
from src.states.entities.BaseEntityState import BaseEntityState


class JumpState(BaseEntityState):
    def enter(self) -> None:
        self.entity.change_animation("jump")
        self.entity.vy = -settings.GRAVITY / 2
        settings.SOUNDS["jump"].play()

    def update(self, dt: float) -> None:
        self.entity.vy += settings.GRAVITY * dt

        # If there is a collision on the right, correct x. Else, correct x if there is collision on the left.
        self.entity.handle_tilemap_collision_on_right() or self.entity.handle_tilemap_collision_on_left()

        if self.entity.handle_tilemap_collision_on_top():
            self.entity.vy = 0

        if self.entity.vy >= 0:
            self.entity.change_state("fall")

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if self.entity.player_type == 1:
            if input_id == "move_left":
                if input_data.pressed:
                    self.entity.vx = -settings.PLAYER_SPEED
                    self.entity.flipped = True
                    self.entity.direcction = settings.LEFT 
                elif input_data.released and self.entity.vx <= 0:
                    self.entity.vx = 0
            elif input_id == "move_right":
                if input_data.pressed:
                    self.entity.vx = settings.PLAYER_SPEED
                    self.entity.flipped = False
                    self.entity.direcction = settings.RIGHT 
                elif input_data.released and self.entity.vx >= 0:
                    self.entity.vx = 0
        else :
            if input_id == "move_left_p2":
                if input_data.pressed:
                    self.entity.vx = -settings.PLAYER_SPEED
                    self.entity.flipped = True
                    self.entity.direcction = settings.LEFT 
                elif input_data.released and self.entity.vx <= 0:
                    self.entity.vx = 0
            elif input_id == "move_right_p2":
                if input_data.pressed:
                    self.entity.vx = settings.PLAYER_SPEED
                    self.entity.flipped = False
                    self.entity.direcction = settings.RIGHT
                elif input_data.released and self.entity.vx >= 0:
                    self.entity.vx = 0

