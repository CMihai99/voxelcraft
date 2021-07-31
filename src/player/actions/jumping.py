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

class Jump(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui, # Specifies parent of the movement which is the player
        )

    def update(self):
        if held_keys['space down']:
            player.y += 1
            invoke(setattr, player, 'y', player.y - 1) # 1 block height
