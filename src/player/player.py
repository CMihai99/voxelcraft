'''
-----------------------------------------------------------------------------------------
Copyright (c) 2023 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
-----------------------------------------------------------------------------------------
'''

# Import module
from ursina import *

# Sound
hit_sound = Audio('.../resources/player/sounds/hit', loop = False, autoplay = False)

class Player(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui
            )
