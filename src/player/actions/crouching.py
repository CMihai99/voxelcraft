'''
===-----------------------------------------------------------------------------------===
Copyright (c) 2021 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
===-----------------------------------------------------------------------------------===
'''

from ursina import *

# Import components
from player import firstpersoncontroller

# Components
player = firstpersoncontroller.Player() # Map the player to the 1st person view

class Crouch(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui, # Specifies parent of the movement which is the player
        )

    def update(self):
        if held_keys['shift']:
            player.crouching = True
            base_speed = 8
            crouch_speed = base_speed / 4
            player.speed = lerp(base_speed, crouch_speed, 0.5) # Smoother dynamic crouching
            player.camera.position = (0, -1, 0) # 1.5 block height
        else:
            player.crouching = False
            base_speed = 8
            crouch_speed = base_speed / 2
            player.speed = lerp(base_speed, crouch_speed, 1)   # Smoother dynamic crouching
            player.camera.position = (0, -1/1.33, 0) # 2 block height
