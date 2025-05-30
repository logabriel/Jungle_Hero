"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class FallState for player.
"""

from gale.input_handler import InputData

import settings
from src.states.entities.BaseEntityState import BaseEntityState


class FallState(BaseEntityState):
    def enter(self) -> None:
        self.entity.change_animation("jump")
        self.point_initial = self.entity.y + self.entity.height
    
    def exit(self) -> None:
        self.point_final = self.entity.y + self.entity.height

        if abs(self.point_initial - self.point_initial) >= self.entity.tilemap.tileheight * 20:
            self.entity.is_dead = True

    def update(self, dt: float) -> None:
        self.entity.vy += settings.GRAVITY * dt

        # If there is a collision on the right, correct x. Else, correct x if there is collision on the left.
        self.entity.handle_tilemap_collision_on_right() or self.entity.handle_tilemap_collision_on_left()

        if self.entity.handle_tilemap_collision_on_bottom():
            self.entity.vy = 0
            if self.entity.vx > 0:
                self.entity.change_state("walk", "right")
            elif self.entity.vx < 0:
                self.entity.change_state("walk", "left")
            else:
                self.entity.change_state("idle")

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
