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

from blocks.blocks import Blocks
from player.player import Player
from player.arm import Arm
from inventory.inventory import Inventory

from player.actions.zoom import Zoom
from player.actions.walk import Walk
from player.actions.sprint import Sprint
from player.actions.crouch import Crouch
from player.actions.jump import Jump

from controls import MainControls
from blocks.controls import BlocksControls
from player.controls import PlayerControls
from inventory.controls import InventoryControls

# Link file components
Sky()
# Terrain()

Blocks()
Player()
Arm()
Inventory()

Zoom()
Walk()
Sprint()
Crouch()
Jump()

MainControls()
BlocksControls()
PlayerControls()
InventoryControls()
