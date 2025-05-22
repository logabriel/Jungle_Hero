"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class PlayState.
"""

from typing import Dict, Any

import pygame

from gale.input_handler import InputData
from gale.state import BaseState
from gale.text import render_text
from gale.timer import Timer

import settings
from src.Camera import Camera
from src.Clock import Clock
from src.GameLevel import GameLevel
from src.Player import Player
from src.GameItem import GameItem
from src.Tile import Tile
from src.definitions import tiles, level

class PlayState(BaseState):
    def enter(self, **enter_params: Dict[str, Any]) -> None:
        self.level = enter_params.get("level", 1)
        self.game_level = enter_params.get("game_level")
        self.num_players = enter_params.get("num_players", 1)
        self.definition = level.LEVEL[self.level]
        self.spanw_player_1_x = self.definition.get("position_player1_x", 0)
        self.spawn_player_1_y = self.definition.get("position_player1_y", 0)
        self.spanw_player_2_x = self.definition.get("position_player2_x", 0)
        self.spawn_player_2_y = self.definition.get("position_player2_y", 0)

        if self.game_level is None:
            self.game_level = GameLevel(self.level)
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load(
                    settings.BASE_DIR / "assets" / "sounds" / "play_game.ogg"
                )
                pygame.mixer.music.play(loops=-1)

        self.tilemap = self.game_level.tilemap
        
        players_param = enter_params.get("players")
        if players_param is None:
            self.players = [None, None]
        else:
            self.players = players_param + [None] * (2 - len(players_param))
            
        # Creamos jugadores
        if self.players[0] is None:
            self.players[0] = Player(self.spanw_player_1_x, self.spawn_player_1_y, 1, self.game_level)
            self.players[0].change_state("idle")
        else:
            self.players[0].game_level = self.game_level
            self.players[0].tilemap = self.tilemap
        
        if self.num_players == 2:
            if self.players[1] is None:
                self.players[1] = Player(self.spanw_player_2_x, self.spawn_player_2_y, 2, self.game_level)
                self.players[1].change_state("idle")
            else:
                self.players[1].game_level = self.game_level
                self.players[1].tilemap = self.tilemap
        else:
            # Si es 1 jugador
            self.players[1] = None
            
        self.camera = enter_params.get("camera")

        if self.camera is None:
            self.camera = Camera(0, 0, settings.VIRTUAL_WIDTH, settings.VIRTUAL_HEIGHT)
            self.camera.set_collision_boundaries(self.game_level.get_rect())

            if self.num_players == 2:
                self.camera.attach_to([self.players[0], self.players[1]])
            else:
                self.camera.attach_to(self.players[0])

        self.clock = enter_params.get("clock")

        if self.clock is None:
            self.clock = Clock(self.definition["time_play"])

            def countdown_timer():
                self.clock.count_down()

                if 0 < self.clock.time <= 5:
                    settings.SOUNDS["timer"].play()

                if self.clock.time == 0:
                    self.players[0].change_state("dead")
                    if self.num_players == 2 and self.players[1]:
                        self.players[1].change_state("dead")

            Timer.every(1, countdown_timer)
        else:
            Timer.resume()
        
        # Set the golden key and golden block as inactive.
        for item in self.game_level.items:
            if item.texture_id == "key-gold":
                if item.frame_index == 0:
                    self.itemKey = item
                    self.itemKey.active = False
                elif item.frame_index == 8:
                    self.itemBLock = item
                    self.itemBLock.active = False

        self.score_next_level = 200 + self.level * 28

    def update(self, dt: float) -> None:
        # Verificar muerte de jugadores activos
        if self.players[0].is_dead or (self.num_players == 2 and self.players[1] and self.players[1].is_dead):
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            Timer.clear()
            self.state_machine.change("game_over", self.players)

        for player in self.players:
            if player is None:
                continue
            player.update(dt)

            if player.y >= player.tilemap.height:
                player.change_state("dead")

            self.camera.update()
            self.game_level.set_render_boundaries(self.camera.get_rect())
            self.game_level.update(dt)

            for creature in self.game_level.creatures:
                if player.collides(creature):
                    player.change_state("dead")

            for item in self.game_level.items:
                if not item.active or not item.collidable:
                    continue

                if player.collides(item):
                    item.on_collide(player)
                    item.on_consume(player)

            if Player.girl_save == self.game_level.girls_to_rescue:
                self.game_level.winNextLevel = True
                player.score = 0
                Timer.clear()
                players_to_pass = [p for p in self.players if p is not None]
                self.state_machine.change("transition", players=self.players, level=self.level)
                return

    def render(self, surface: pygame.Surface) -> None:
        world_surface = pygame.Surface((self.tilemap.width, self.tilemap.height))
        self.game_level.render(world_surface)
        
        for player in self.players:
            if player is not None:
                player.render(world_surface)
        
        surface.blit(world_surface, (-self.camera.x, -self.camera.y))

        # Mostrar "girls" salvadas y tiempo
        render_text(
            surface,
            f"girl save: {Player.girl_save}",
            settings.FONTS["small"],
            5,
            5,
            (255, 255, 255),
            shadowed=True,
        )

        render_text(
            surface,
            f"Time: {self.clock.time}",
            settings.FONTS["small"],
            settings.VIRTUAL_WIDTH - 65,
            5,
            (255, 255, 255),
            shadowed=True,
        )

    def on_input(self, input_id: str, input_data: InputData) -> None:
        if input_id == "pause" and input_data.pressed:
            Timer.pause()
            self.state_machine.change(
                "pause",
                level=self.level,
                camera=self.camera,
                game_level=self.game_level,
                players=self.players,
                clock=self.clock,
            )
        else:
            for player in self.players:
                if player is not None:
                    player.on_input(input_id, input_data)

    # Genera un bloque sólido en la primera capa
    def generate_item_block(self) -> None:
        item_i = self.tilemap.to_i(self.itemBLock.y)
        item_j = self.tilemap.to_j(self.itemBLock.x)          
        self.tilemap.layers[0][item_i][item_j] = Tile(item_i, item_j, 16, 16, 41, dict(top=True, right=True, bottom=True, left=True))
