"""
-----------------------------------------------------------------------------------------
Copyright (c) 2023 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
-----------------------------------------------------------------------------------------
"""

# Import module
from ursina import *
# Import module component
from ursina.prefabs.first_person_controller import FirstPersonController

# Import file which stores file components
from __init__ import *

# Declare game
game = Ursina()

# Link module component
ursina_player = FirstPersonController()

# Window settings
window.title = "Voxelcraft Beta 1.0.0"
window.icon = "/resources/blocks/textures/grass.png"
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = False

# Run game
game.run()
