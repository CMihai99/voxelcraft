"""
-----------------------------------------------------------------------------------------
Copyright (c) 2023 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
-----------------------------------------------------------------------------------------
"""

# Import module
from ursina import *

# Import file component
from main import ursina_player


class Zoom(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui
        )

    def update(self):
        # If 'c' key is held, player is zooming
        if held_keys["c"]:
            ursina_player.zoom = True
            camera.fov /= 1.33
            ursina_player.x /= 1.33
        # Player isn't zooming
        else:
            ursina_player.zoom = False
            camera.fov = camera.fov
            ursina_player.x = ursina_player.x
