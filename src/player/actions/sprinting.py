'''
===-----------------------------------------------------------------------------------===
Copyright (c) 2021 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
===-----------------------------------------------------------------------------------===
'''

from ursina import *

# Import components
from player import firstpersoncontroller

# Map the player to the 1st person view
player = firstpersoncontroller.Player()

class Sprint(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui
        )

    def update(self):
        if held_keys['control'] and held_keys['w'] and player.crouching is False:
            player.sprinting = True
            base_speed = 8
            sprint_speed = base_speed * 4
            # Smoother dynamic speed
            player.speed = lerp(base_speed, sprint_speed, 2)
            base_fov = 90
            sprint_fov = 100
            # Smoother dynamic FOV
            player.camera.fov = lerp(base_fov, sprint_fov, 1)

        else:
            player.sprinting = False
            base_speed = 8
            sprint_speed = base_speed * 2
            # Smoother dynamic speed
            player.speed = lerp(sprint_speed, base_speed, 4)
            base_fov = 90
            sprint_fov = 100
            # Smoother dynamic FOV
            player.camera.fov = lerp(sprint_fov, base_fov, 2)
