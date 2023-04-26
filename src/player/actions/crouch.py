"""
-----------------------------------------------------------------------------------------
Copyright (c) 2023 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
-----------------------------------------------------------------------------------------
"""

# Import module
from ursina import *

# Import file components
from main import ursina_player
from player.actions.walk import walk_speed

crouch_speed = walk_speed / 5


class Crouch(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui
        )

    def update(self):
        # If 'shift' key is held and player isn't walking or sprinting,
        # player is crouching
        if (
            held_keys["shift"]
            and ursina_player.walk == False
            and ursina_player.sprint == False
        ):
            ursina_player.crouch = True
            ursina_player.speed = lerp(walk_speed, crouch_speed, 0.5)  # Smooth speed transition
            ursina_player.origin_y = ursina_player.origin_y - 1  # Crouch 1 block
        # Player isn't crouching
        else:
            ursina_player.crouch = False
            ursina_player.speed = lerp(crouch_speed, walk_speed, 1)  # Smooth speed transition
            ursina_player.origin_y = ursina_player.origin_y  # Default height
