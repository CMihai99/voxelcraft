'''
-----------------------------------------------------------------------------------------
Copyright (c) 2023 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
-----------------------------------------------------------------------------------------
'''

# Import module
from ursina import *

# Textures
slot_texture = load_texture('.../resources/inventory/textures/empty_slot')
shield_slot_texture = load_texture('.../resources/inventory/textures/shield_slot')
boots_slot_texture = load_texture('.../resources/inventory/textures/boots_slot')
leggings_slot_texture = load_texture('.../resources/inventory/textures/leggings_slot')
chestplate_slot_texture = load_texture('.../resources/inventory/textures/chestplate_slot')
helmet_slot_texture = load_texture('.../resources/inventory/textures/helmet_slot')

class Inventory(Entity):
    class Hotbar(Entity):
        def __init__(self, **kwargs):
            super().__init__(
                parent = camera.ui,
                model = Quad(radius = 0),
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
                    grid_positions = [(int(e.x * self.texture_scale[0]),
                                       int(e.y * self.texture_scale[1]))
                                       for e in self.children]
                    # print(grid_positions)

                    if not (x, -y) in grid_positions:
                        # print('found free spot:', x, y)
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
                x = x * 1 / self.texture_scale[0],
                y = -y * 1 / self.texture_scale[1],
                z = -.5,
            )

            def drag():
                icon.org_pos = (icon.x, icon.y)
                # Ensure that the dragged item overlaps the rest
                icon.z -= .01

            def drop():
                icon.x = int((icon.x + (icon.scale_x / 2)) * 9) / 9
                icon.y = int((icon.y - (icon.scale_y / 2)) * 1) / 1
                icon.z += .01

                # If outside, return to original position
                if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                    icon.position = (icon.org_pos)
                    return

                # If spot is taken, swap positions
                for c in self.children:
                    if c == icon:
                        continue
                    if c.x == icon.x and c.y == icon.y:
                        c.position = icon.org_pos

            icon.drag = drag
            icon.drop = drop

    class LowerInventory(Entity):
        def __init__(self, **kwargs):
            super().__init__(
                parent = camera.ui,
                model = Quad(radius = 0),
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
                    grid_positions = [(int(e.x * self.texture_scale[0]),
                                       int(e.y * self.texture_scale[1]))
                                       for e in self.children]
                    # print(grid_positions)

                    if not (x, -y) in grid_positions:
                        # print('found free spot:', x, y)
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
                # Ensure that the dragged item overlaps the rest
                icon.z -= .01

            def drop():
                icon.x = int((icon.x + (icon.scale_x / 2)) * 9) / 9
                icon.y = int((icon.y - (icon.scale_y / 2)) * 3) / 3
                icon.z += .01

                # If outside, return to original position
                if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                    icon.position = (icon.org_pos)
                    return

                # If spot is taken, swap positions
                for c in self.children:
                    if c == icon:
                        continue
                    if c.x == icon.x and c.y == icon.y:
                        c.position = icon.org_pos

            icon.drag = drag
            icon.drop = drop

    class ShieldSlot(Entity):
        def __init__(self, **kwargs):
            super().__init__(
                parent = camera.ui,
                model = Quad(radius = 0),
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
                    grid_positions = [(int(e.x * self.texture_scale[0]),
                                       int(e.y * self.texture_scale[1]))
                                       for e in self.children]
                    # print(grid_positions)

                    if not (x, -y) in grid_positions:
                        # print('found free spot:', x, y)
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
                # Ensure that the dragged item overlaps the rest
                icon.z -= .01

            def drop():
                icon.x = int((icon.x + (icon.scale_x / 2)) * 1) / 1
                icon.y = int((icon.y - (icon.scale_y / 2)) * 1) / 1
                icon.z += .01

                # If outside, return to original position
                if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                    icon.position = (icon.org_pos)
                    return

                # If spot is taken, swap positions
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

    class BootsSlot(Entity):
        def __init__(self, **kwargs):
            super().__init__(
                parent = camera.ui,
                model = Quad(radius = 0),
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
                    grid_positions = [(int(e.x * self.texture_scale[0]),
                                       int(e.y * self.texture_scale[1]))
                                       for e in self.children]
                    # print(grid_positions)

                    if not (x, -y) in grid_positions:
                        # print('found free spot:', x, y)
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
                # Ensure that the dragged item overlaps the rest
                icon.z -= .01

            def drop():
                icon.x = int((icon.x + (icon.scale_x / 2)) * 1) / 1
                icon.y = int((icon.y - (icon.scale_y / 2)) * 1) / 1
                icon.z += .01

                # If outside, return to original position
                if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                    icon.position = (icon.org_pos)
                    return

                # If spot is taken, swap positions
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

    class LeggingsSlot(Entity):
        def __init__(self, **kwargs):
            super().__init__(
                parent= camera.ui,
                model = Quad(radius = 0),
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
                    grid_positions = [(int(e.x * self.texture_scale[0]),
                                       int(e.y * self.texture_scale[1]))
                                       for e in self.children]
                    # print(grid_positions)

                    if not (x, -y) in grid_positions:
                        # print('found free spot:', x, y)
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
                # Ensure that the dragged item overlaps the rest
                icon.z -= .01

            def drop():
                icon.x = int((icon.x + (icon.scale_x / 2)) * 1) / 1
                icon.y = int((icon.y - (icon.scale_y / 2)) * 1) / 1
                icon.z += .01

                # If outside, return to original position
                if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                    icon.position = (icon.org_pos)
                    return

                # If spot is taken, swap positions
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

    class ChestplateSlot(Entity):
        def __init__(self, **kwargs):
            super().__init__(
                parent = camera.ui,
                model = Quad(radius = 0),
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
                    grid_positions = [(int(e.x * self.texture_scale[0]),
                                       int(e.y * self.texture_scale[1]))
                                       for e in self.children]
                    # print(grid_positions)

                    if not (x, -y) in grid_positions:
                        # print('found free spot:', x, y)
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
                # Ensure that the dragged item overlaps the rest
                icon.z -= .01

            def drop():
                icon.x = int((icon.x + (icon.scale_x / 2)) * 1) / 1
                icon.y = int((icon.y - (icon.scale_y / 2)) * 1) / 1
                icon.z += .01

                # If outside, return to original position
                if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                    icon.position = (icon.org_pos)
                    return

                # If spot is taken, swap positions
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

    class HelmetSlot(Entity):
        def __init__(self, **kwargs):
            super().__init__(
                parent = camera.ui,
                model = Quad(radius = 0),
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
                    grid_positions = [(int(e.x * self.texture_scale[0]),
                                       int(e.y * self.texture_scale[1]))
                                       for e in self.children]
                    # print(grid_positions)

                    if not (x, -y) in grid_positions:
                        # print('found free spot:', x, y)
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
                # Ensure that the dragged item overlaps the rest
                icon.z -= .01

            def drop():
                icon.x = int((icon.x + (icon.scale_x / 2)) * 1) / 1
                icon.y = int((icon.y - (icon.scale_y / 2)) * 1) / 1
                icon.z += .01

                # If outside, return to original position
                if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                    icon.position = (icon.org_pos)
                    return

                # If spot is taken, swap positions
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

    class InventoryCraftingGrid(Entity):
        def __init__(self, **kwargs):
            super().__init__(
                parent = camera.ui,
                model = Quad(radius = 0),
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
                    grid_positions = [(int(e.x * self.texture_scale[0]),
                                       int(e.y * self.texture_scale[1]))
                                       for e in self.children]
                    # print(grid_positions)

                    if not (x, -y) in grid_positions:
                        # print('found free spot:', x, y)
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
                # Ensure that the dragged item overlaps the rest
                icon.z -= .01

            def drop():
                icon.x = int((icon.x + (icon.scale_x / 2)) * 2) / 2
                icon.y = int((icon.y - (icon.scale_y / 2)) * 2) / 2
                icon.z += .01

                # If outside, return to original position
                if icon.x < 0 or icon.x >= 1 or icon.y > 0 or icon.y <= -1:
                    icon.position = (icon.org_pos)
                    return

                # If spot is taken, swap positions
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

    class InventoryCraftingOutput(Entity):
        def __init__(self, **kwargs):
            super().__init__(
                parent = camera.ui,
                model = Quad(radius = 0),
                texture = slot_texture,
                texture_scale = (1, 1),
                scale = (0.08, 0.08),
                origin = (1.12, -2.27),
                position = (0.42, -0.02),
                color = color.rgb(255, 255, 255)
            )

            for key, value in kwargs.items():
                setattr(self, key, value)
