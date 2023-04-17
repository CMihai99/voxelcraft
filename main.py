'''
-----------------------------------------------------------------------------------------
Copyright (c) 2023 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
-----------------------------------------------------------------------------------------
'''

# Original idea: https://github.com/pokepetter/ursina/blob/master/samples/minecraft_clone.py

# Import module
from ursina import *
# Import components
from ursina.prefabs.first_person_controller import FirstPersonController
from player import arm
from player.actions import sprinting, crouching, zooming
from world.sky import main

app = Ursina() # Declare program

# Map components
sky = main.Sky()
player = FirstPersonController()
arm = arm.Arm()

sprinting = sprinting.Sprint()
crouching = crouching.Crouch()
zooming = zooming.Zoom()

# Textures
grass_texture = load_texture('/resources/blocks/textures/grass.png')
dirt_texture = load_texture('/resources/blocks/textures/dirt.png')
stone_texture = load_texture('/resources/blocks/textures/stone.png')
cobblestone_texture = load_texture('/resources/blocks/textures/cobblestone.png')

slot_texture = load_texture('/resources/inventory/empty_slot.png')
shield_slot_texture = load_texture('/resources/inventory/shield_slot.png')
boots_slot_texture = load_texture('/resources/inventory/boots_slot.png')
leggings_slot_texture = load_texture('/resources/inventory/leggings_slot.png')
chestplate_slot_texture = load_texture('/resources/inventory/chestplate_slot.png')
helmet_slot_texture = load_texture('/resources/inventory/helmet_slot.png')

# Sounds
hit_sound = Audio('/resources/player/arm/hit', loop = False, autoplay = False)

# Window settings
window.title = 'Voxelcraft Beta 1.0.0'
window.icon = load_texture('/resources/blocks/textures/grass.png')
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = False

# Player inventory
class Inventory(Entity):
    class Hotbar(Entity):
        def __init__(self, **kwargs):
            super().__init__(
                parent = camera.ui,
                model = Quad(radius=0),
                texture = slot_texture,
                texture_scale = (9, 1),
                scale = (0.72, 0.08),
                origin = (-0.32, 0.62),
                position = (-0.23, -0.315),
                color = color.rgb(255, 255, 255)
            )

            for key, value in kwargs.items():
                setattr(self, key, value)

        def find_free_spot(self):
            for y in range(1):
                for x in range(9):
                    grid_positions = [(int(e.x * self.texture_scale[0]), int(e.y * self.texture_scale[1]))
                                      for e in self.children]
                    print(grid_positions)

                    if not (x, -y) in grid_positions:
                        print('found free spot:', x, y)
                        return x, y

        # Add items
        def append(self, item, x = 0, y = 0):
            if len(self.children) >= 9 * 1:
                return

            x, y = self.find_free_spot()

            icon = Draggable(
                parent = self,
                model = 'quad',
                texture = item,
                color = color.white,
                scale_x = 1 / self.texture_scale[0],
                scale_y = 1 / self.texture_scale[1],
                origin = (-.5, .5),
                x= x * 1 / self.texture_scale[0],
                y= -y * 1 / self.texture_scale[1],
                z= -.5,
            )

            def drag():
                icon.org_pos = (icon.x, icon.y)
                # Ensure the dragged item overlaps the rest
                icon.z -= .01

            def drop():
                icon.x = int((icon.x + (icon.scale_x / 2)) * 9) / 9
                icon.y = int((icon.y - (icon.scale_y / 2)) * 1) / 1
                icon.z += .01

                # If outside, return to original position
                if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                    icon.position = (icon.org_pos)
                    return

                # If the spot is taken, swap positions
                for c in self.children:
                    if c == icon:
                        continue
                    if c.x == icon.x and c.y == icon.y:
                        c.position = icon.org_pos

            icon.drag = drag
            icon.drop = drop

    class Lower_Inventory(Entity):
        def __init__(self, **kwargs):
            super().__init__(
                parent = camera.ui,
                model = Quad(radius=0),
                texture = slot_texture,
                texture_scale = (9, 3),
                scale = (0.72, 0.24),
                origin = (-0.32, 0.62),
                position = (-0.23, -0.03),
                color = color.rgb(255, 255, 255)
            )

            for key, value in kwargs.items():
                setattr(self, key, value)

        def find_free_spot(self):
            for y in range(3):
                for x in range(9):
                    grid_positions = [(int(e.x * self.texture_scale[0]), int(e.y * self.texture_scale[1]))
                                      for e in self.children]
                    print(grid_positions)

                    if not (x, -y) in grid_positions:
                        print('found free spot:', x, y)
                        return x, y

        # Add items
        def append(self, item, x = 0, y = 0):
            if len(self.children) >= 9 * 3:
                return

            x, y = self.find_free_spot()

            icon = Draggable(
                parent = self,
                model = 'quad',
                texture = item,
                color = color.white,
                scale_x = 1 / self.texture_scale[0],
                scale_y = 1 / self.texture_scale[1],
                origin = (-.5, .5),
                x = x * 1 / self.texture_scale[0],
                y = -y * 1 / self.texture_scale[1],
                z = -.5,
            )

            def drag():
                icon.org_pos = (icon.x, icon.y)
                # Ensure the dragged item overlaps the rest
                icon.z -= .01

            def drop():
                icon.x = int((icon.x + (icon.scale_x / 2)) * 9) / 9
                icon.y = int((icon.y - (icon.scale_y / 2)) * 3) / 3
                icon.z += .01

                # If outside, return to original position
                if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                    icon.position = (icon.org_pos)
                    return

                # If the spot is taken, swap positions
                for c in self.children:
                    if c == icon:
                        continue
                    if c.x == icon.x and c.y == icon.y:
                        c.position = icon.org_pos

            icon.drag = drag
            icon.drop = drop

    class Shield_Slot(Entity):
        def __init__(self, **kwargs):
            super().__init__(
                parent = camera.ui,
                model = Quad(radius=0),
                texture = shield_slot_texture,
                texture_scale = (1, 1),
                scale = (0.08, 0.08),
                origin = (1.12, -2.27),
                position = (0.08, -0.18),
                color = color.rgb(255, 255, 255)
            )

            for key, value in kwargs.items():
                setattr(self, key, value)

        def find_free_spot(self):
            for y in range(1):
                for x in range(1):
                    grid_positions = [(int(e.x * self.texture_scale[0]), int(e.y * self.texture_scale[1]))
                                      for e in self.children]
                    print(grid_positions)

                    if not (x, -y) in grid_positions:
                        print('found free spot:', x, y)
                        return x, y

        # Add item
        def append(self, item, x = 0, y = 0):
            if len(self.children) >= 1 * 1:
                return

            x, y = self.find_free_spot()

            icon = Draggable(
                parent = self,
                model = 'quad',
                texture = item,
                color = color.white,
                scale_x = 1 / self.texture_scale[0],
                scale_y = 1 / self.texture_scale[1],
                origin = (-.5, .5),
                x = x * 1 / self.texture_scale[0],
                y = -y * 1 / self.texture_scale[1],
                z = -.5,
            )

            def drag():
                icon.org_pos = (icon.x, icon.y)
                # Ensure the dragged item overlaps the rest
                icon.z -= .01

            def drop():
                icon.x = int((icon.x + (icon.scale_x / 2)) * 1) / 1
                icon.y = int((icon.y - (icon.scale_y / 2)) * 1) / 1
                icon.z += .01

                # If outside, return to original position
                if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                    icon.position = (icon.org_pos)
                    return

                # If the spot is taken, swap positions
                for c in self.children:
                    if c == icon:
                        continue
                    if c.x == icon.x and c.y == icon.y:
                        c.position = icon.org_pos

            icon.drag = drag
            icon.drop = drop

            # def add_item(): # Can only add shields
            # global shield
            # inventory.append(shield)

    class Boots_Slot(Entity):
        def __init__(self, **kwargs):
            super().__init__(
                parent = camera.ui,
                model = Quad(radius=0),
                texture = boots_slot_texture,
                texture_scale = (1, 1),
                scale = (0.08, 0.08),
                origin = (1.12, -2.27),
                position = (-0.23, -0.18),
                color = color.rgb(255, 255, 255)
            )

            for key, value in kwargs.items():
                setattr(self, key, value)

        def find_free_spot(self):
            for y in range(1):
                for x in range(1):
                    grid_positions = [(int(e.x * self.texture_scale[0]), int(e.y * self.texture_scale[1]))
                                      for e in self.children]
                    print(grid_positions)

                    if not (x, -y) in grid_positions:
                        print('found free spot:', x, y)
                        return x, y

        # Add item
        def append(self, item, x = 0, y = 0):
            if len(self.children) >= 1 * 1:
                return

            x, y = self.find_free_spot()

            icon = Draggable(
                parent = self,
                model = 'quad',
                texture = item,
                color = color.white,
                scale_x = 1 / self.texture_scale[0],
                scale_y = 1 / self.texture_scale[1],
                origin = (-.5, .5),
                x = x * 1 / self.texture_scale[0],
                y = -y * 1 / self.texture_scale[1],
                z = -.5,
            )

            def drag():
                icon.org_pos = (icon.x, icon.y)
                # Ensure the dragged item overlaps the rest
                icon.z -= .01

            def drop():
                icon.x = int((icon.x + (icon.scale_x / 2)) * 1) / 1
                icon.y = int((icon.y - (icon.scale_y / 2)) * 1) / 1
                icon.z += .01

                # If outside, return to original position
                if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                    icon.position = (icon.org_pos)
                    return

                # If the spot is taken, swap positions
                for c in self.children:
                    if c == icon:
                        continue
                    if c.x == icon.x and c.y == icon.y:
                        c.position = icon.org_pos

            icon.drag = drag
            icon.drop = drop

            # def add_item(): # Can only add boots
            # global iron_boots
            # inventory.append(iron_boots)

    class Leggings_Slot(Entity):
        def __init__(self, **kwargs):
            super().__init__(
                parent= camera.ui,
                model = Quad(radius=0),
                texture = leggings_slot_texture,
                texture_scale = (1, 1),
                scale = (0.08, 0.08),
                origin = (1.12, -2.27),
                position = (-0.23, -0.1),
                color = color.rgb(255, 255, 255)
            )

            for key, value in kwargs.items():
                setattr(self, key, value)

        def find_free_spot(self):
            for y in range(1):
                for x in range(1):
                    grid_positions = [(int(e.x * self.texture_scale[0]), int(e.y * self.texture_scale[1]))
                                      for e in self.children]
                    print(grid_positions)

                    if not (x, -y) in grid_positions:
                        print('found free spot:', x, y)
                        return x, y

        # Add item
        def append(self, item, x = 0, y = 0):
            if len(self.children) >= 1 * 1:
                return

            x, y = self.find_free_spot()

            icon = Draggable(
                parent = self,
                model = 'quad',
                texture = item,
                color = color.white,
                scale_x = 1 / self.texture_scale[0],
                scale_y = 1 / self.texture_scale[1],
                origin = (-.5, .5),
                x = x * 1 / self.texture_scale[0],
                y = -y * 1 / self.texture_scale[1],
                z = -.5,
            )

            def drag():
                icon.org_pos = (icon.x, icon.y)
                # Ensure the dragged item overlaps the rest
                icon.z -= .01

            def drop():
                icon.x = int((icon.x + (icon.scale_x / 2)) * 1) / 1
                icon.y = int((icon.y - (icon.scale_y / 2)) * 1) / 1
                icon.z += .01

                # If outside, return to original position
                if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                    icon.position = (icon.org_pos)
                    return

                # If the spot is taken, swap positions
                for c in self.children:
                    if c == icon:
                        continue
                    if c.x == icon.x and c.y == icon.y:
                        c.position = icon.org_pos

            icon.drag = drag
            icon.drop = drop

            # def add_item(): # Can only add leggings
            # global iron_leggings
            # inventory.append(iron_leggings)

    class Chestplate_Slot(Entity):
        def __init__(self, **kwargs):
            super().__init__(
                parent = camera.ui,
                model = Quad(radius=0),
                texture = chestplate_slot_texture,
                texture_scale = (1, 1),
                scale = (0.08, 0.08),
                origin = (1.12, -2.27),
                position = (-0.23, -0.02),
                color = color.rgb(255, 255, 255)
            )

            for key, value in kwargs.items():
                setattr(self, key, value)

        def find_free_spot(self):
            for y in range(1):
                for x in range(1):
                    grid_positions = [(int(e.x * self.texture_scale[0]), int(e.y * self.texture_scale[1]))
                                      for e in self.children]
                    print(grid_positions)

                    if not (x, -y) in grid_positions:
                        print('found free spot:', x, y)
                        return x, y

        # Add item
        def append(self, item, x = 0, y = 0):
            if len(self.children) >= 1 * 1:
                return

            x, y = self.find_free_spot()

            icon = Draggable(
                parent = self,
                model = 'quad',
                texture = item,
                color = color.white,
                scale_x = 1 / self.texture_scale[0],
                scale_y = 1 / self.texture_scale[1],
                origin = (-.5, .5),
                x = x * 1 / self.texture_scale[0],
                y = -y * 1 / self.texture_scale[1],
                z = -.5,
            )

            def drag():
                icon.org_pos = (icon.x, icon.y)
                # Ensure the dragged item overlaps the rest
                icon.z -= .01

            def drop():
                icon.x = int((icon.x + (icon.scale_x / 2)) * 1) / 1
                icon.y = int((icon.y - (icon.scale_y / 2)) * 1) / 1
                icon.z += .01

                # If outside, return to original position
                if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                    icon.position = (icon.org_pos)
                    return

                # If the spot is taken, swap positions
                for c in self.children:
                    if c == icon:
                        continue
                    if c.x == icon.x and c.y == icon.y:
                        c.position = icon.org_pos

            icon.drag = drag
            icon.drop = drop

            # def add_item(): # Can only add chestplates
            # global iron_chestplate
            # inventory.append(iron_chestplate)

    class Helmet_Slot(Entity):
        def __init__(self, **kwargs):
            super().__init__(
                parent = camera.ui,
                model = Quad(radius=0),
                texture = helmet_slot_texture,
                texture_scale = (1, 1),
                scale = (0.08, 0.08),
                origin  = (1.12, -2.27),
                position = (-0.23, 0.06),
                color = color.rgb(255, 255, 255)
            )

            for key, value in kwargs.items():
                setattr(self, key, value)

        def find_free_spot(self):
            for y in range(1):
                for x in range(1):
                    grid_positions = [(int(e.x * self.texture_scale[0]), int(e.y * self.texture_scale[1]))
                                      for e in self.children]
                    print(grid_positions)

                    if not (x, -y) in grid_positions:
                        print('found free spot:', x, y)
                        return x, y

        # Add item
        def append(self, item, x = 0, y = 0):
            if len(self.children) >= 1 * 1:
                return

            x, y = self.find_free_spot()

            icon = Draggable(
                parent = self,
                model = 'quad',
                texture = item,
                color = color.white,
                scale_x = 1 / self.texture_scale[0],
                scale_y = 1 / self.texture_scale[1],
                origin = (-.5, .5),
                x = x * 1 / self.texture_scale[0],
                y = -y * 1 / self.texture_scale[1],
                z = -.5,
            )

            def drag():
                icon.org_pos = (icon.x, icon.y)
                # Ensure the dragged item overlaps the rest
                icon.z -= .01

            def drop():
                icon.x = int((icon.x + (icon.scale_x / 2)) * 1) / 1
                icon.y = int((icon.y - (icon.scale_y / 2)) * 1) / 1
                icon.z += .01

                # If outside, return to original position
                if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                    icon.position = (icon.org_pos)
                    return

                # If the spot is taken, swap positions
                for c in self.children:
                    if c == icon:
                        continue
                    if c.x == icon.x and c.y == icon.y:
                        c.position = icon.org_pos

            icon.drag = drag
            icon.drop = drop

            # def add_item(): # Can only add helmets
            # global iron_helmet
            # inventory.append(iron_helmet)

    class Inventory_Crafting_Grid(Entity):
        def __init__(self, **kwargs):
            super().__init__(
                parent = camera.ui,
                model = Quad(radius=0),
                texture = slot_texture,
                texture_scale = (2, 2),
                scale = (0.16, 0.16),
                origin = (1.12, -2.27),
                position = (0.3, -0.2),
                color = color.rgb(255, 255, 255)
            )

            for key, value in kwargs.items():
                setattr(self, key, value)

        def find_free_spot(self):
            for y in range(2):
                for x in range(2):
                    grid_positions = [(int(e.x * self.texture_scale[0]), int(e.y * self.texture_scale[1]))
                                      for e in self.children]
                    print(grid_positions)

                    if not (x, -y) in grid_positions:
                        print('found free spot:', x, y)
                        return x, y

        # Add items
        def append(self, item, x = 0, y = 0):
            if len(self.children) >= 2 * 2:
                return

            x, y = self.find_free_spot()

            icon = Draggable(
                parent = self,
                model = 'quad',
                texture = item,
                color = color.white,
                scale_x = 1 / self.texture_scale[0],
                scale_y = 1 / self.texture_scale[1],
                origin = (-.5, .5),
                x = x * 1 / self.texture_scale[0],
                y = -y * 1 / self.texture_scale[1],
                z = -.5,
            )

            def drag():
                icon.org_pos = (icon.x, icon.y)
                # Ensure the dragged item overlaps the rest
                icon.z -= .01

            def drop():
                icon.x = int((icon.x + (icon.scale_x / 2)) * 2) / 2
                icon.y = int((icon.y - (icon.scale_y / 2)) * 2) / 2
                icon.z += .01

                # If outside, return to original position
                if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                    icon.position = (icon.org_pos)
                    return

                # If the spot is taken, swap positions
                for c in self.children:
                    if c == icon:
                        continue
                    if c.x == icon.x and c.y == icon.y:
                        c.position = icon.org_pos

            icon.drag = drag
            icon.drop = drop

            # def add_item(): # Can only add helmets
            # global iron_helmet
            # inventory.append(iron_helmet)

    class Inventory_Crafting_Output(Entity):
        def __init__(self, **kwargs):
            super().__init__(
                parent = camera.ui,
                model = Quad(radius=0),
                texture = slot_texture,
                texture_scale = (1, 1),
                scale = (0.08, 0.08),
                origin = (1.12, -2.27),
                position = (0.42, -0.02),
                color = color.rgb(255, 255, 255)
            )

            for key, value in kwargs.items():
                setattr(self, key, value)

# def update():
#     Inventory().Hotbar() # Show hotbar at all times

#     # Open inventory
#     if held_keys['e']:
#         # application.pause()
#         # Show mouse
#         mouse.locked = False

#         Inventory().Lower_Inventory()
#         Inventory().Boots_Slot()
#         Inventory().Leggings_Slot()
#         Inventory().Chestplate_Slot()
#         Inventory().Helmet_Slot()
#         Inventory().Shield_Slot()
#         Inventory().Inventory_Crafting_Grid()
#         Inventory().Inventory_Crafting_Output()
#     else:
#         # application.resume()
#         # Hide mouse
#         mouse.locked = True

# Blocks
block_pick = 1 # Default block is the grass block

class Voxel(Button):
    def __init__(self, position = (0, 0, 0), texture = grass_texture):
        # Ends up with the grass texture being selected as default
        super().__init__(
            parent = scene,
            position = position,
            model = "resources/blocks/models/block",
            origin_y = 2.25,
            color = color.color(0, 0, random.uniform(0.9, 1)),
            texture = texture,
            scale = 1
        )

    # Key input
    def input(self, key):
        global block_pick

        if self.hovered:
            # If number 1 button is pressed
            if key == '1':
                block_pick = 1 # Pick grass block
            # If number 2 button is pressed
            if key == '2':
                block_pick = 2 # Pick dirt block
            # If number 3 button is pressed
            if key == '3':
                block_pick = 3 # Pick stone block
            # If number 4 button is pressed
            if key == '4':
                block_pick = 4 # Pick cobblestone block

            # If left mouse button is pressed
            if key == 'left mouse down':
                arm.active() # Arm animation is active

                destroy(self) # Break block

                hit_sound.play() # Play hit sound
            else:
                arm.passive() # Arm animation is passive

            # If right mouse button is pressed
            if key == 'right mouse down':
                hit_sound.play() # Play hit sound

                # Place block
                if block_pick == 1: Voxel(position=self.position + mouse.normal,
                                                    texture=grass_texture) # Place grass block
                if block_pick == 2: Voxel(position=self.position + mouse.normal,
                                                    texture=dirt_texture)  # Place dirt block
                if block_pick == 3: Voxel(position=self.position + mouse.normal,
                                                    texture=stone_texture) # Place stone block
                if block_pick == 4: Voxel(position=self.position + mouse.normal,
                                                    texture=cobblestone_texture) # Place cobblestone block

            # If escape button is pressed
            if key == 'escape':
                exit() # Exit program

# Generate map
for x in range(16): # 16 blocks on the x-axis
    for y in range(4): # 4 blocks on the y-axis
        for z in range(16): # 16 blocks on the z-axis
            Voxel(position=(x, y, z))

app.run() # Run program
