import pygame

from gale.animation import Animation
from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import Text, render_text
from gale.timer import Timer

import settings

class CharacterSelectState(BaseState):
    def enter(self) -> None:
        self.options = ["1 Jugador", "2 Jugadores"]
        self.selected_index = 0

    def exit(self) -> None:
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        
    def update(self, dt: float) -> None:
        pass

    def render(self, surface: pygame.Surface) -> None:
        surface.blit(settings.TEXTURES["blue_bg"], (0, 0))

        render_text(
            surface,
            "Selecciona",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 4 - 20,
            (197, 195, 198),
            center=True,
            shadowed=True,
        )
        render_text(
            surface,
            "número de jugadores",
            settings.FONTS["medium"],
            settings.VIRTUAL_WIDTH // 2,
            settings.VIRTUAL_HEIGHT // 4 + 20,
            (197, 195, 198),
            center=True,
            shadowed=True,
        )

        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i == self.selected_index else (150, 150, 150)
            render_text(
                surface,
                option,
                settings.FONTS["small"],
                settings.VIRTUAL_WIDTH // 2,
                settings.VIRTUAL_HEIGHT // 2 + i * 30,
                color,
                center=True,
                shadowed=True,
            )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id in ("up", "move_up_p1", "move_up_p2") and input_data.pressed:
            self.selected_index = (self.selected_index - 1) % len(self.options)
        elif input_id in ("down", "move_down_p1", "move_down_p2") and input_data.pressed:
            self.selected_index = (self.selected_index + 1) % len(self.options)
        elif input_id == "enter" and input_data.pressed:
            if self.selected_index == 0:
                self.state_machine.change("play", num_players=1, players=[None, None])
            else:
                self.state_machine.change("play", num_players=2, players=[None, None])


