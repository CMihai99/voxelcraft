'''
-----------------------------------------------------------------------------------------
Copyright (c) 2023 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
-----------------------------------------------------------------------------------------
'''

# Import module
from ursina import *

# Import file component
from main import ursina_player

# Sound
hit_sound = Audio('/resources/player/sounds/hit.wav', loop = False, autoplay = False)

class Player(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            origin_y = 2.5 # 2.5 block height
        )
