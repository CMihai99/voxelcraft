# Getting Started
Voxelcraft is an open-source project written in [the ursina engine](https://github.com/pokepetter/ursina), simulating the popular game Minecraft.

Check project wikis for more in-depth information.


# Installation
To run the program use the following command:

```pip install -r requirements.txt```

and then run [main.py](https://github.com/CMihai99/nesucraft/blob/main/main.py).


# Game

## Controls

W - move up

A - strafe left

S - move down

D - strafe right

1 - change current block to grass (default)

2 - change current block to dirt

3 - change current block to stone

4 - change current block to cobblestone

Left mouse button - break block

Right mouse button - place block

Shift - crouch

Ctrl - sprint

Space - jump

Esc - menu


## Problems

FOV increase should be based on time delta, its too sudden currently (line 123).

Crouching needs to be smoother, add time delta to camera position change (line 135).

Grass texture needs to have its own voxel settings so that the top and bottom texture won't the same (line 61).


## License
[MIT License](https://choosealicense.com/licenses/mit/)
