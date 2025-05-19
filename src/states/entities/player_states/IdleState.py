"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class IdleState for player.
"""

from gale.input_handler import InputData

from src.states.entities.BaseEntityState import BaseEntityState
import settings


class IdleState(BaseEntityState):
    def enter(self) -> None:
        self.entity.vx = 0
        self.entity.vy = 0
        self.entity.change_animation("idle")

    def update(self, dt: float) -> None:
        if self.entity.handle_tilemap_collision_on_bottom():
            self.entity.vy = 0

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if self.entity.player_type == 1:
            if input_id == "move_left" and input_data.pressed:
                self.entity.flipped = True
                self.entity.direcction = settings.LEFT 
                self.entity.change_state("walk", "left")
            elif input_id == "move_right" and input_data.pressed:
                self.entity.flipped = True
                self.entity.direcction = settings.RIGHT 
                self.entity.change_state("walk", "right")
            elif input_id == "jump" and input_data.pressed:
                self.entity.change_state("jump")
            elif input_id == "attack" and input_data.pressed:
                if self.entity.direcction == settings.RIGHT:
                    self.entity.change_state("attack", "right")
                else :
                    self.entity.change_state("attack", "left")
        else : 
            if input_id == "move_left_p2" and input_data.pressed:
                self.entity.flipped = True
                self.entity.direcction = settings.LEFT 
                self.entity.change_state("walk", "left")
            elif input_id == "move_right_p2" and input_data.pressed:
                self.entity.flipped = True
                self.entity.direcction = settings.RIGHT 
                self.entity.change_state("walk", "right")
            elif input_id == "jump_p2" and input_data.pressed:
                self.entity.change_state("jump")
            elif input_id == "attack_p2" and input_data.pressed:
                if self.entity.direcction == settings.RIGHT:
                    self.entity.change_state("attack", "right")
                else :
                    self.entity.change_state("attack", "left")
            
