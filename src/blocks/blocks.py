'''
-----------------------------------------------------------------------------------------
Copyright (c) 2023 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
-----------------------------------------------------------------------------------------
'''

# Import module
from ursina import *

# Textures
grass_texture = load_texture('../resources/blocks/textures/grass')
dirt_texture = load_texture('../resources/blocks/textures/dirt')
stone_texture = load_texture('../resources/blocks/textures/stone')
cobblestone_texture = load_texture('../resources/blocks/textures/cobblestone')

# Default block is the grass block
block_pick = 1

class Blocks(Entity):
    def __init__(self):
        super().__init__(
            parent = scene,
            model = '../resources/blocks/models/block',
            color = color.color(0, 0, random.uniform(0.9, 1)),
            scale = 1
            )
