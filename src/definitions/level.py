import settings
from typing import Dict, Any

LEVEL: Dict[int, Dict[str, Any]] = {
    1: {
        "position_player1_x": 0,
        "position_player1_y": settings.VIRTUAL_HEIGHT - 66,
        "position_player2_x": 0,
        "position_player2_y": settings.VIRTUAL_HEIGHT - 66,
        "girls_to_rescue": 2,
        "time_play": 120
    },
    2: {
        "position_player1_x": 0,
        "position_player1_y": settings.VIRTUAL_HEIGHT - 66,
        "position_player2_x": 0,
        "position_player2_y": settings.VIRTUAL_HEIGHT - 66,
        "girls_to_rescue": 2,
        "time_play": 180
    },
    3: {
        "position_player1_x": 0,
        "position_player1_y": settings.VIRTUAL_HEIGHT - 66,
        "position_player2_x": 0,
        "position_player2_y": settings.VIRTUAL_HEIGHT - 66,
        "girls_to_rescue": 3,
        "time_play": 180
    },
    4: {
        "position_player1_x": 0,
        "position_player1_y": 160,
        "position_player2_x": 0,
        "position_player2_y": 160,
        "girls_to_rescue": 4,
        "time_play": 180 #en segundos
    },
    5: {
        "position_player1_x": 224,
        "position_player1_y": 160,
        "position_player2_x": 224,
        "position_player2_y": 160,
        "girls_to_rescue": 1,
        "time_play": 220 #en segundos
    },
    6: {
        "position_player1_x": 32 * 48,
        "position_player1_y": 32 * 2,
        "position_player2_x": 32 * 48,
        "position_player2_y": 32 * 2 ,
        "girls_to_rescue": 5,
        "time_play": 180 #en segundos
    },
}
