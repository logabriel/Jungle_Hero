import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import render_text

import settings

class WinState(BaseState):
    def enter(self, players) -> None:
        pygame.mixer.music.load(
            settings.BASE_DIR / "assets" / "sounds" / "victory.ogg"
        )
        pygame.mixer.music.play(start=3.0)
        self.players = players

    def exit(self) -> None:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "enter" and input_data.pressed:
            self.state_machine.change("start")

    def render(self, surface: pygame.Surface) -> None:
        jungle_bg = settings.TEXTURES["jungle_bg"]
        surface.blit(
            pygame.transform.scale(
                jungle_bg,
                (settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT)
            ),
            (0, 0)
        )

        render_text(
            surface,
            "You won, congratulations, you are a hero!",
            settings.FONTS["small"],
            settings.VIRTUAL_WIDTH // 2,
            40,
            (255, 255, 255),
            center=True,
            shadowed=True,
        )

        render_text(
            surface,
            "Press enter to start",
            settings.FONTS["small"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT - 40,
            (255, 255, 255),
            center=True,
            shadowed=True,
        )
