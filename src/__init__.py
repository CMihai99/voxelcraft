"""
-----------------------------------------------------------------------------------------
Copyright (c) 2023 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
-----------------------------------------------------------------------------------------
"""

# Import file components
from world.sky import Sky
# from world.terrain import Terrain
from controls import MainControls

from blocks.blocks import Blocks
from blocks.controls import BlocksControls

from player.player import Player
from player.arm import Arm
from player.actions.zoom import Zoom
from player.actions.walk import Walk
from player.actions.sprint import Sprint
from player.actions.crouch import Crouch
from player.actions.jump import Jump
from player.controls import PlayerControls

from inventory.inventory import Inventory
from inventory.controls import InventoryControls

# Link file components
Sky()
# Terrain()
MainControls()

Blocks()
BlocksControls()

Player()
Arm()
Zoom()
Walk()
Sprint()
Crouch()
Jump()
PlayerControls()

Inventory()
InventoryControls()
