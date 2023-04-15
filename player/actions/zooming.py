'''
===-----------------------------------------------------------------------------------===
Copyright (c) 2021 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
===-----------------------------------------------------------------------------------===
'''

from ursina import *

# Import components
from ursina.prefabs.first_person_controller import FirstPersonController

# Map the player to the 1st person view
player = FirstPersonController()

class Zoom(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui
        )

    def update(self):
        if held_keys['c']:
            player.zoom = True
            camera.fov /= 1.33
            player.x /= 1.33

        else:
            player.zoom = False
            camera.fov = camera.fov
            player.x = player.x
