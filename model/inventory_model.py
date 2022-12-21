import os
import json


class Inventory:
    def __init__(self):
        self.inventory_path = "database/inventory.json"

    def save_inventory(self, inventory):
        inventory_list = self.retrieve_inventory()
        inventory_list.append(inventory)
        self.write_to_inventory_list(inventory_list)

    def retrieve_inventory(self):
        inventory_list = []
        if os.path.exists(self.inventory_path):
            with open(self.inventory_path, 'r') as f:
                inventory_list = json.load(f)
        return inventory_list

    def update_inventory(self, item_id, n_inventory):
        inventory_list = self.retrieve_inventory()
        for i in range(len(inventory_list)):
            inventory_object = inventory_list[i]
            if inventory_object['id'] == item_id:
                inventory_list.remove(inventory_object)
                inventory_list.insert(i, n_inventory)
        self.write_to_inventory_list(inventory_list)

    def delete_inventory(self, item_id):
        inventory_list = self.retrieve_inventory()
        for inventory_object in inventory_list:
            if inventory_object['id'] == item_id:
                inventory_list.remove(inventory_object)
        self.write_to_inventory_list(inventory_list)
    
    def write_to_inventory_list(self, inventory_list):
        with open(self.inventory_path, 'w') as f:
            json.dump(inventory_list, f, indent=True)
