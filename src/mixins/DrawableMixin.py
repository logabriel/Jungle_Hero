"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the DrawableMixin.
"""

import pygame

import settings


class DrawableMixin:
    def render(self, surface: pygame.Surface) -> None:
        texture = settings.TEXTURES[self.texture_id]
        frame = settings.FRAMES[self.texture_id][self.frame_index]
        image = pygame.Surface((frame.width, frame.height), pygame.SRCALPHA)
        image.fill((0, 0, 0, 0))
        image.blit(texture, (0, 0), frame)

        if self.flipped:
            image = pygame.transform.flip(image, True, False)

        surface.blit(image, (self.x, self.y))

        #debug
        #rect = pygame.Rect(self.x, self.y, frame.width, frame.height)
        #pygame.draw.rect(surface, (255, 0, 0), rect, 2)  # Rojo, grosor 2
