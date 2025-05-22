"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Camera.
"""

import pygame

from src.GameEntity import GameEntity

class Camera:
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.collision_boundaries = None
        self.following = []  

    def attach_to(self, entities) -> None:
        if isinstance(entities, list):
            self.following = [e for e in entities if e is not None]
        else:
            self.following = [entities]

    def set_collision_boundaries(self, rect: pygame.Rect) -> None:
        self.collision_boundaries = rect

    def update(self) -> None:
        if self.following:
            xs = [entity.x + entity.width // 2 for entity in self.following]
            ys = [entity.y + entity.height // 2 for entity in self.following]

            center_x = sum(xs) / len(xs)
            center_y = sum(ys) / len(ys)

            self.x = int(center_x - self.width // 2)
            self.y = int(center_y - self.height // 2)

        if self.collision_boundaries is not None:
            self.x = max(
                self.collision_boundaries.x,
                min(
                    self.x,
                    self.collision_boundaries.x
                    + self.collision_boundaries.width
                    - self.width,
                ),
            )
            self.y = max(
                self.collision_boundaries.y,
                min(
                    self.y,
                    self.collision_boundaries.y
                    + self.collision_boundaries.height
                    - self.height,
                ),
            )

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)
