"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the definition for creatures.
"""

from typing import Dict, Any

from src.states.entities import creatures_states

SNAKE = 0
HIENA = 16
WHITE_HUMAN = 32
AXE_HUMAN = 63
SCORPION = 64

CREATURES: Dict[int, Dict[str, Any]] = {
    SNAKE: {
        "texture_id": "creatures",
        "walk_speed": 8,
        "animation_defs": {"walk": {"frames": [4, 5, 6, 7, 8, 9], "interval": 0.30}},
        "states": {"walk": creatures_states.SnailWalkState},
        "first_state": "walk",
        "sound" : "snake_dead",
    },
    HIENA: {
        "texture_id": "creatures",
        "walk_speed": 24,
        "animation_defs": {"walk": {"frames": [19, 20, 21, 22, 23, 24, 25], "interval": 0.18}},
        "states": {"walk": creatures_states.SnailWalkState},
        "first_state": "walk",
        "sound" : "hyena_dead",
    },
    WHITE_HUMAN: {
        "texture_id": "creatures",
        "walk_speed": 12,
        "animation_defs": {"walk": {"frames": [36, 37, 38, 39, 40, 41], "interval": 0.28}},
        "states": {"walk": creatures_states.SnailWalkState},
        "first_state": "walk",
        "sound" : "man_dead_1",
    },
    AXE_HUMAN: {
        "texture_id": "creatures",
        "walk_speed": 14,
        "animation_defs": {"walk": {"frames": [60, 59, 58, 57, 56], "interval": 0.32}},
        "states": {"walk": creatures_states.SnailWalkState},
        "first_state": "walk",
        "sound" : "man_dead_2",
    },
    SCORPION: {
        "texture_id": "creatures",
        "walk_speed": 6,
        "animation_defs": {"walk": {"frames": [67, 68, 69, 70, 71, 72, 73], "interval": 0.30}},
        "states": {"walk": creatures_states.SnailWalkState},
        "first_state": "walk",
        "sound" : "scorpion_dead",
    },
}
