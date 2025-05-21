"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class GameOverState.
"""

import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import render_text
from src.Player import Player

import settings


class GameOverState(BaseState):
    def enter(self, players) -> None:
        self.players = players

    def exit(self) -> None:
        Player.girl_save_total = 0

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "enter" and input_data.pressed:
            self.state_machine.change("start")

    def render(self, surface: pygame.Surface) -> None:
        blue_bg = settings.TEXTURES["blue_bg"]
        jungle_bg = settings.TEXTURES["game_over_bg"]

        surface.blit(
            pygame.transform.scale(
                blue_bg,
                (settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT)
            ),
            (0, 0)
        )
        
        surface.blit(
            pygame.transform.scale(
                jungle_bg,
                (settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT)
            ),
            (0, 0)
        )

        render_text(
            surface,
            "Game Over!",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            20,
            (255, 255, 255),
            center=True,
            shadowed=True,
        )

        y = 50

        render_text(
            surface,
            f"total number of girls rescued: {Player.girl_save_total}",
            settings.FONTS["small"],
            settings.VIRTUAL_WIDTH // 2,
            y + 10,
            (255, 255, 255),
            shadowed=True,
            center=True,
        )

        render_text(
            surface,
            "Press Enter to play again",
            settings.FONTS["small"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT - 20,
            (255, 255, 255),
            center=True,
            shadowed=True,
        )
