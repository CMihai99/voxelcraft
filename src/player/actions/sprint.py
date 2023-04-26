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
from player.actions.walk import walk_speed, walk_fov

sprint_speed = walk_speed * 5
sprint_fov = walk_fov + 20


class Sprint(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui
        )

    def update(self):
        # If 'control' and 'w' keys are held and player isn't walking
        # or crouching, player is sprinting
        if (
            held_keys["control" and "w"]
            and ursina_player.walk == False
            and ursina_player.crouch == False
        ):
            ursina_player.sprint = True
            ursina_player.speed = lerp(walk_speed, sprint_speed, 2)  # Smooth speed transition
            camera.fov = lerp(walk_fov, sprint_fov, 1)  # Smooth FOV transition
        # Player isn't sprinting
        else:
            ursina_player.sprint = False
            ursina_player.speed = lerp(sprint_speed, walk_speed, 4)  # Smooth speed transition
            camera.fov = lerp(sprint_fov, walk_fov, 2)  # Smooth FOV transition
