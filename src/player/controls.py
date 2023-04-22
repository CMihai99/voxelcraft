"""
-----------------------------------------------------------------------------------------
Copyright (c) 2023 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
-----------------------------------------------------------------------------------------
"""

# Import module
from ursina import *

# Import file components
from player.player import hit_sound
from player.arm import Arm


class PlayerControls(Entity):
    def input(self, key):
        if self.hovered:
            # If left mouse button is pressed
            if key == "left mouse down":
                Arm().active()  # Arm animation is active

                hit_sound.play()  # Play hit sound
            else:
                Arm().passive()  # Arm animation is passive

            # If right mouse button is pressed, play hit sound
            if key == "right mouse down":
                hit_sound.play()
