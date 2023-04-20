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

# Import file components
from main import ursina_player
from walking import walk_speed

crouch_speed = walk_speed / 5

class Crouch(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui
            )

    def update(self):
        if held_keys['shift'] and ursina_player.walk is False and ursina_player.sprint is False:
            ursina_player.crouch = True
            ursina_player.speed = lerp(walk_speed, crouch_speed, 0.5) # Smooth speed transition
            ursina_player.origin_y = ursina_player.origin_y - 1 # Crouch 1 block
        else:
            ursina_player.crouch = False
            ursina_player.speed = lerp(crouch_speed, walk_speed, 1) # Smooth speed transition
            ursina_player.origin_y = ursina_player.origin_y # Default height
