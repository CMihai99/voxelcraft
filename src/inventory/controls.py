'''
-----------------------------------------------------------------------------------------
Copyright (c) 2023 Voxelcraft

For copying notice, see https://github.com/CMihai99/voxelcraft/blob/main/COPYING.
For licenses we use, see https://github.com/CMihai99/voxelcraft/tree/main/LICENSES.
-----------------------------------------------------------------------------------------
'''

# Import module
from ursina import *

# Import file component
from inventory import Inventory

class InventoryControls(Entity):
    def input(self, key):
        if self.hovered:
            Inventory.Hotbar() # Show hotbar at all times

            # Open inventory
            if key == 'e':
                application.pause()
                mouse.locked = False # Show mouse
                # mouse.visible = False # Show mouse

                Inventory.LowerInventory()
                Inventory.BootsSlot()
                Inventory.LeggingsSlot()
                Inventory.ChestplateSlot()
                Inventory.HelmetSlot()
                Inventory.ShieldSlot()
                Inventory.InventoryCraftingGrid()
                Inventory.InventoryCraftingOutput()
            else:
                application.resume()
                mouse.locked = True # Hide mouse
                # mouse.visible = True # Hide mouse
