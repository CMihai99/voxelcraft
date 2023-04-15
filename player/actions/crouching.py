'''
===-----------------------------------------------------------------------------------===
Copyright (c) 2021 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
===-----------------------------------------------------------------------------------===
'''

from ursina import *

# Import components
from ursina.prefabs.first_person_controller import FirstPersonController
from player.actions.vs import Values
# Map the player to the 1st person view
player = FirstPersonController()
values = Values()

class Crouch(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui
        )

    def update(self):
        if held_keys['shift']:
            values.crouching = True
            base_speed = 8
            crouch_speed = base_speed / 4
            # Smoother dynamic crouching
            player.speed = lerp(base_speed, crouch_speed, 0.5)
            player.position = (0, -1, 0) # 1.5 block height

        else:
            values.crouching = False
            base_speed = 8
            crouch_speed = base_speed / 2
            # Smoother dynamic crouching
            player.speed = lerp(base_speed, crouch_speed, 1)
            player.position = (0, -1/1.33, 0) # 2 block height
