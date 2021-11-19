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

class Jump(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui
        )

    def update(self):
        if held_keys['space down']:
            player.y += 1
            invoke(setattr, player, 'y', player.y - 1) # 1 block height
