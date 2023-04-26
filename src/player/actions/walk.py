"""
-----------------------------------------------------------------------------------------
Copyright (c) 2023 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
-----------------------------------------------------------------------------------------
"""

# Import module
from ursina import *

# Declare variables early to prevent circular imports
walk_speed = 10
walk_fov = 80

# Import file components
from main import ursina_player
from player.actions.crouch import crouch_speed
from player.actions.sprint import sprint_speed


class Walk(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui
        )

    def update(self):
        # If player is crouching, player isn't walking
        if ursina_player.crouch:
            ursina_player.walk = False
            ursina_player.speed = crouch_speed
        # If player is sprinting, player isn't walking
        if ursina_player.sprint:
            ursina_player.walk = False
            ursina_player.speed = sprint_speed
        # Player is walking
        else:
            ursina_player.walk = True
            ursina_player.speed = walk_speed
