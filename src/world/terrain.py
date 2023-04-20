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
sys.path.append('..')

# Import file component
from blocks.blocks import Blocks

class Terrain(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			double_sided = True # See terrain when in it
			)

	def generate(self):
		for x in range(16): # 16 blocks on the x-axis
			for y in range(4): # 4 blocks on the y-axis
				for z in range(16): # 16 blocks on the z-axis
					Blocks(position = (x, y, z), origin_y = 2.25) # OR origin_y = 2.5
