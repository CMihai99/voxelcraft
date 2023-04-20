'''
-----------------------------------------------------------------------------------------
Copyright (c) 2023 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
-----------------------------------------------------------------------------------------
'''

# Import module
from ursina import *

# Import module component
from ursina.prefabs.first_person_controller import FirstPersonController

# Import file components
from world.sky import Sky
from world.terrain import Terrain

from blocks.blocks import Blocks
from player.player import Player
from player.arm import Arm
from inventory.inventory import Inventory

from player.actions.zooming import Zoom
from player.actions.walking import Walk
from player.actions.sprinting import Sprint
from player.actions.crouching import Crouch

from controls import MainControls
from blocks.controls import BlocksControls
from player.controls import PlayerControls
from inventory.controls import InventoryControls

# Declare program
app = Ursina()

# Map module component
ursina_player = FirstPersonController()

# Map file components
Sky()
Terrain()

Blocks()
Player()
Arm()
Inventory()

Zoom()
Walk()
Sprint()
Crouch()

MainControls()
BlocksControls()
PlayerControls()
InventoryControls()

# Window settings
window.title = 'Voxelcraft Beta 1.0.0'
window.icon = load_texture('../resources/blocks/textures/grass')
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = False

# Run program
app.run()
