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

# Components
player = firstpersoncontroller.Player() # Map the player to the 1st person view

class Zoom(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui, # Specifies parent of the movement which is the player
        )

    def update(self):
        if held_keys['c']:
            player.zoom = True
            player.camera.fov = player.camera.fov / 1.33
            player.camera.x = player.camera.x / 1.33
        else:
            player.zoom = False
            player.camera.fov = player.camera.fov
            player.camera.x = player.camera.x
