"""
This file contains the class AttackState for player.
"""

from gale.input_handler import InputData
from gale.timer import Timer

from src.states.entities.BaseEntityState import BaseEntityState
from src.Hitbox import Hitbox

import settings

class AttackState(BaseEntityState):
    def enter(self, direction: str) -> None:
        self.entity.play_characteristic_sound() #reproduce su sonido caracteristico

        self.entity.flipped = direction == "left"
        self.entity.vx = 0
        self.entity.vy = 0
        self.entity.change_animation("attack")
        
        self.hitboxWidth = 12
        self.hitboxHeight = 31
        
        if self.entity.direcction == settings.LEFT:
            self.hitboxX = self.entity.x - self.hitboxWidth
            self.hitboxY = self.entity.y
        elif self.entity.direcction == settings.RIGHT:
            self.hitboxX = self.entity.x + self.entity.width
            self.hitboxY = self.entity.y

        self.swordHitbox = Hitbox(self.hitboxX, self.hitboxY, self.hitboxWidth, self.hitboxHeight)
    
        Timer.after(0.75, lambda: self.entity.change_state("idle"),)
        
    def update(self, dt: float) -> None:
        if self.entity.handle_tilemap_collision_on_bottom():
            self.entity.vy = 0
        
        for entity in self.entity.game_level.creatures:
            if entity.collides(self.swordHitbox):
                entity.play_characteristic_sound()
                entity.is_dead = True

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
