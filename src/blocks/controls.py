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
from blocks import grass_texture, dirt_texture, stone_texture, cobblestone_texture
from blocks import block_pick, Blocks

class BlocksControls(Entity):
    def input(self, key):
        global block_pick

        if self.hovered:
            # If number 1 key is pressed
            if key == '1':
                block_pick = 1 # Pick grass block
            # If number 2 key is pressed
            if key == '2':
                block_pick = 2 # Pick dirt block
            # If number 3 key is pressed
            if key == '3':
                block_pick = 3 # Pick stone block
            # If number 4 key is pressed
            if key == '4':
                block_pick = 4 # Pick cobblestone block

            # If left mouse button is pressed
            if key == 'left mouse down':
                destroy(self) # Break block

            # If right mouse button is pressed
            if key == 'right mouse down':
                # Place block
                if block_pick == 1: Blocks(position = self.position + mouse.normal,
                                            texture = grass_texture) # Place grass block
                if block_pick == 2: Blocks(position = self.position + mouse.normal,
                                            texture = dirt_texture)  # Place dirt block
                if block_pick == 3: Blocks(position = self.position + mouse.normal,
                                            texture = stone_texture) # Place stone block
                if block_pick == 4: Blocks(position = self.position + mouse.normal,
                                            texture = cobblestone_texture) # Place cobblestone block
