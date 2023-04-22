'''
-----------------------------------------------------------------------------------------
Copyright (c) 2023 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
-----------------------------------------------------------------------------------------
'''

# Import module
from ursina import *

# Import file components
from main import ursina_player

class Jump(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui
            )

    def input(self, key):
        if self.hovered:
            # If 'space' key is pressed, player is jumping
            if key == 'space':
                ursina_player.jump = True
                ursina_player.origin_y = ursina_player.origin_y + 1 # Jump 1 block
            # Player isn't jumping
            else:
                ursina_player.jump = False
                ursina_player.origin_y = ursina_player.origin_y # Default height
