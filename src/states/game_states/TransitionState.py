from typing import Dict, Any

import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import render_text
from gale.timer import Timer

import settings
from src.Player import Player
from src.GameLevel import GameLevel
from src.definitions import level

class TransitionState(BaseState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.level = enter_params.get("level") + 1
        self.players = enter_params.get("players")

        if self.level > settings.NUM_LEVELS:
            self.level = 1
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            self.state_machine.change("win", players=self.players)

        self.radius = max(settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT)  
        self.transitioning = True 
        self.definition = level.LEVEL[self.level]
        self.previous_surface = pygame.Surface((settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT))
        game_level = GameLevel(self.level)
        game_level.render(self.previous_surface)
        
        for player in self.players:
            player.render(self.previous_surface)
            player.girl_save = 0
            player.vx = 0
            player.vy = 0
            player.x = self.definition.get("position_player1_x")
            player.y = self.definition.get("position_player1_y")

    def update(self, dt: float) -> None:
        if self.transitioning:
            self.radius -= 300 * dt 
            if self.radius <= 0:
                self.transitioning = False  

    def render(self, surface: pygame.Surface) -> None:
        if self.transitioning:
            
            surface.blit(self.previous_surface, (0, 0))

            
            mask_surface = pygame.Surface((settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT), pygame.SRCALPHA)
            mask_surface.fill((0, 0, 0, 255))  

            pygame.draw.circle(
                mask_surface,
                (0, 0, 0, 0),  
                (settings.VIRTUAL_WIDTH // 2, settings.VIRTUAL_HEIGHT // 2),
                max(0, int(self.radius)),
            )

            surface.blit(mask_surface, (0, 0))
        else:
            surface.fill((0, 0, 0)) 
            render_text(
                surface,
                f"Next level {self.level}",
                settings.FONTS["medium"],
                settings.VIRTUAL_WIDTH // 2,
                20,
                (255, 255, 255),
                center=True,
                shadowed=True,
            )
            render_text(
                surface,
                "press enter to continue",
                settings.FONTS["medium"],
                settings.VIRTUAL_WIDTH // 2,
                settings.VIRTUAL_HEIGHT // 2,
                (197, 195, 198),
                center=True,
                shadowed=True,
            )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if not self.transitioning and input_id == "enter" and input_data.pressed:
            self.state_machine.change(
                "play",
                level=self.level,
                players=self.players,
            )

