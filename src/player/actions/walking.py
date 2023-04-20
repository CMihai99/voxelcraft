'''
-----------------------------------------------------------------------------------------
Copyright (c) 2023 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
-----------------------------------------------------------------------------------------
'''

# Import modules
from ursina import *
import sys

# Move beyond top level
sys.path.append('...')

# Import file component
from main import ursina_player
from crouching import crouch_speed
from sprinting import sprint_speed

walk_speed = 10
walk_fov = 80

class Walk(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui
            )

    def update(self):
        if ursina_player.crouch is True:
            ursina_player.walk = False
            walk_speed = crouch_speed
        if ursina_player.sprint is True:
            ursina_player.walk = False
            walk_speed = sprint_speed
        else:
            ursina_player.walk = True
            walk_speed = walk_speed
