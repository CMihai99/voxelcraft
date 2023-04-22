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
from inventory.inventory import Inventory

class InventoryControls(Entity):
    Inventory.Hotbar() # Show hotbar at all times

    def input(self, key):
        if self.hovered:
            # If 'e' key is pressed
            if key == 'e':
                # Open inventory
                Inventory.LowerInventory()
                Inventory.BootsSlot()
                Inventory.LeggingsSlot()
                Inventory.ChestplateSlot()
                Inventory.HelmetSlot()
                Inventory.ShieldSlot()
                Inventory.InventoryCraftingGrid()
                Inventory.InventoryCraftingOutput()

                # application.pause()
                mouse.locked = False # Show mouse
                # mouse.visible = True # Show mouse
            else:
                # Close inventory
                destroy(Inventory.LowerInventory())
                destroy(Inventory.BootsSlot())
                destroy(Inventory.LeggingsSlot())
                destroy(Inventory.ChestplateSlot())
                destroy(Inventory.HelmetSlot())
                destroy(Inventory.ShieldSlot())
                destroy(Inventory.InventoryCraftingGrid())
                destroy(Inventory.InventoryCraftingOutput())

                # application.resume()
                mouse.locked = True # Hide mouse
                # mouse.visible = False # Hide mouse
