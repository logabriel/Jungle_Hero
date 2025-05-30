"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class StartState.
"""

import pygame

from gale.animation import Animation
from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import Text, render_text
from gale.timer import Timer

import settings


class StartState(BaseState):
    def arrive(self):
        self.tweening = False
        self.martian_animation = Animation([settings.FRAMES["robber"][0]])

    def enter(self) -> None:
        self.title = Text(
            "Jungle Hero",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH,
            settings.VIRTUAL_HEIGHT // 4,
            (197, 195, 198),
            shadowed=True,
        )
        self.title_end_x = settings.VIRTUAL_WIDTH // 2 - self.title.rect.width // 2
        self.martian_x = -16
        self.martian_end_x = settings.VIRTUAL_WIDTH // 2 - 8
        self.martian_texture = settings.TEXTURES["robber"]
        self.martian_animation = Animation(settings.FRAMES["robber"][4:9], 0.15)

        self.tweening = True

        pygame.mixer.music.load(
            settings.BASE_DIR / "assets" / "sounds" / "Menu_audio.ogg"
        )
        pygame.mixer.music.play()
        Timer.tween(
            5,
            [
                (self.title, {"x": self.title_end_x}),
                (self, {"martian_x": self.martian_end_x}),
            ],
            on_finish=self.arrive,
        )

    def update(self, dt: float) -> None:
        self.martian_animation.update(dt)

    def render(self, surface: pygame.Surface) -> None:
        jungle_bg = settings.TEXTURES["jungle_bg"]

        surface.blit(
            pygame.transform.scale(
                jungle_bg,
                (settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT)
            ),
            (0, 0)
        )

        self.title.render(surface)
        surface.blit(
            self.martian_texture,
            (self.martian_x, settings.VIRTUAL_HEIGHT // 2 - 10),
            self.martian_animation.get_current_frame(),
        )

        if not self.tweening:
            render_text(
                surface,
                "Press Enter",
                settings.FONTS["small"],
                settings.VIRTUAL_WIDTH // 2,
                settings.VIRTUAL_HEIGHT // 2 + 40,
                (197, 195, 198),
                center=True,
                shadowed=True,
            )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "enter" and input_data.pressed:
            if self.tweening:
                Timer.clear()
                self.title.x = self.title_end_x
                self.martian_x = self.martian_end_x
                self.arrive()
            else:
                self.state_machine.change("character_select")
