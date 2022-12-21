import os
import json


class Sales:
    def __init__(self, inventory_instance):
        self.inventory_instance = inventory_instance
        self.sales_path = "database/sales.json"
        self.sale_inventory_path = "database/sales_inventory.json"
    
    def save_sale(self, sale):
        sale_list = []
        if os.path.exists(self.sales_path):
            with open(self.sales_path, 'r') as f:
                sale_list = json.load(f)
        sale_list.append(sale)
        self.write_to_sales_list(sale_list)
        self.inventory_sold_item(sale['item_id'])

    def inventory_sold_item(self, item_id):
        inventory_list = self.inventory_instance.retrieve_inventory()
        for inventory_object in inventory_list:
            if inventory_object['id'] == item_id:
                sale_inventory_list = self.retrieve_sales_inventory()
                no_match = True
                for sale_inventory in sale_inventory_list:
                    if sale_inventory['id'] == item_id:
                        sale_inventory['quantity'] += 1
                        no_match = False
                    else:
                        no_match = True
                if no_match:
                    inventory_object['quantity'] = 1
                    sale_inventory_list.append(inventory_object)
                self.write_to_sale_inventory_list(sale_inventory_list)

    def retrieve_sales_inventory(self):
        sale_inventory_list = []
        if os.path.exists(self.sale_inventory_path):
            with open(self.sale_inventory_path, 'r') as f:
                sale_inventory_list = json.load(f)
        return sale_inventory_list

    def retrieve_sales(self):
        sale_list = []
        if os.path.exists(self.sales_path):
            with open(self.sales_path, 'r') as f:
                sale_list = json.load(f)
        return sale_list

    def update_sale(self, sale_id, n_sale):
        sale_list = self.retrieve_sales()
        for i in range(len(sale_list)):
            sale_object = sale_list[i]
            if sale_object['sale_id'] == sale_id:
                sale_list.remove(sale_object)
                sale_list.insert(i, n_sale)
        self.write_to_sales_list(sale_list)

    def delete_sale(self, sale_id):
        sale_list = self.retrieve_sales()
        for sale_object in sale_list:
            if sale_object['sale_id'] == sale_id:
                self.inventory_deleted_sale(sale_object)
                sale_list.remove(sale_object)
        self.write_to_sales_list(sale_list)

    def retrieve_sales_inventory(self):
        sale_inventory_list = []
        if os.path.exists(self.sale_inventory_path):
            with open(self.sale_inventory_path, 'r') as f:
                sale_inventory_list = json.load(f)
        return sale_inventory_list

    def inventory_deleted_sale(self, sale_object):
        sale_inventory_list = self.retrieve_sales_inventory()
        no_match = True
        for sale_inventory_object in sale_inventory_list:
            if sale_inventory_object['id'] == sale_object['item_id']:
                if sale_inventory_object['quantity'] > 1:
                    sale_inventory_object['quantity'] -= 1
                else:
                    sale_inventory_object['quantity'] = 1
                    sale_inventory_list.remove(sale_inventory_object)
                self.save_deleted_sale(sale_inventory_object)
                no_match = False
                break
            else:
                no_match = True
        if no_match:
            sale_inventory_list.append(sale_object)
        self.write_to_sale_inventory_list(sale_inventory_list)

    def save_deleted_sale(self, reset_inventory):
        inventory_list = self.inventory_instance.retrieve_inventory()
        no_match = True
        for i in  range(len(inventory_list)):
            inventory_object = inventory_list[i]
            if inventory_object['id'] == reset_inventory['id']:
                inventory_object['quantity'] += 1
                no_match = False
                break
            else:
                no_match = True
        if no_match:
            inventory_list.append(reset_inventory)
        with open(self.inventory_instance.inventory_path, 'w') as f:
            json.dump(inventory_list, f, indent=True)
    
    def write_to_sales_list(self, sale_list):
        with open(self.sales_path, 'w') as f:
            json.dump(sale_list, f, indent=True)
    
    def write_to_sale_inventory_list(self, sale_inventory_list):
        with open(self.sale_inventory_path, 'w') as f:
            json.dump(sale_inventory_list, f, indent=True)
