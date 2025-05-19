"""
ISPPJ1 2024
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the definition for tiles.
"""

from typing import Dict, Any

TILES: Dict[int, Dict[str, Any]] = {
    # Ground
    0: {"solidness": dict(top=True, right=False, bottom=False, left=True)},
    1: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    2: {"solidness": dict(top=True, right=True, bottom=False, left=False)},
    4: {"solidness": dict(top=False, right=False, bottom=True, left=False)},
    6: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    7: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    8: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    9: {"solidness": dict(top=False, right=False, bottom=False, left=False)},
    11: {"solidness": dict(top=False, right=False, bottom=False, left=True)},
    13: {"solidness": dict(top=False, right=True, bottom=False, left=False)},
    14: {"solidness": dict(top=False, right=True, bottom=False, left=False)},
    16: {"solidness": dict(top=False, right=False, bottom=False, left=True)},
    17: {"solidness": dict(top=False, right=False, bottom=False, left=True)},
    18: {"solidness": dict(top=False, right=False, bottom=True, left=False)},
    19: {"solidness": dict(top=False, right=False, bottom=False, left=False)},
    20: {"solidness": dict(top=False, right=False, bottom=False, left=False)},
    21: {"solidness": dict(top=False, right=False, bottom=False, left=False)},
    22: {"solidness": dict(top=False, right=False, bottom=True, left=True)},
    23: {"solidness": dict(top=False, right=False, bottom=True, left=False)},
    24: {"solidness": dict(top=False, right=True, bottom=True, left=False)},
    26: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    28: {"solidness": dict(top=False, right=True, bottom=False, left=False)},
    29: {"solidness": dict(top=True, right=False, bottom=False, left=True)},
    33: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
    34: {"solidness": dict(top=True, right=False, bottom=True, left=True)},
    35: {"solidness": dict(top=True, right=False, bottom=True, left=False)},
    36: {"solidness": dict(top=True, right=True, bottom=True, left=False)},
    38: {"solidness": dict(top=False, right=False, bottom=False, left=True)},
    39: {"solidness": dict(top=False, right=False, bottom=False, left=True)},
    40: {"solidness": dict(top=False, right=False, bottom=False, left=True)},
    41: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    44: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    45: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    46: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    47: {"solidness": dict(top=False, right=True, bottom=False, left=False)},
    48: {"solidness": dict(top=False, right=True, bottom=False, left=False)},
    49: {"solidness": dict(top=False, right=True, bottom=False, left=False)},
    # 50: {"solidness": dict(top=F, right=False, bottom=False, left=True)},
    40: {"solidness": dict(top=False, right=False, bottom=False, left=True)},
    41: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    44: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    45: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    46: {"solidness": dict(top=True, right=False, bottom=False, left=False)},
    47: {"solidness": dict(top=False, right=True, bottom=False, left=False)},
    48: {"solidness": dict(top=False, right=True, bottom=False, left=False)},
    49: {"solidness": dict(top=False, right=True, bottom=False, left=False)},
    # 50: {"solidness": dict(top=False, right=False, bottom=False, left=False)}, no usar rampas
    # 51: {"solidness": dict(top=False, right=False, bottom=False, left=False)},
    # 52: {"solidness": dict(top=False, right=False, bottom=False, left=False)},
    55: {"solidness": dict(top=False, right=False, bottom=True, left=False)},
    56: {"solidness": dict(top=False, right=False, bottom=True, left=False)},
    57: {"solidness": dict(top=False, right=False, bottom=True, left=False)},
    58: {"solidness": dict(top=True, right=True, bottom=False, left=True)},
    59: {"solidness": dict(top=False, right=True, bottom=False, left=True)},
    60: {"solidness": dict(top=False, right=True, bottom=True, left=True)},
    64: {"solidness": dict(top=True, right=True, bottom=True, left=True)},
}
