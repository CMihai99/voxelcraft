'''
-----------------------------------------------------------------------------------------
Copyright (c) 2023 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
-----------------------------------------------------------------------------------------
'''

# Import module
from ursina import *

class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = 'cube',
            # texture = '../resources/world/sky/textures/sky.png',
            color = color.rgb(95, 175, 255),
            scale = 1000,
            double_sided = True # See sky when inside it
        )
