import csv
import os

class InventoryModel:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        if not os.path.exists(self.csv_file):
            self._create_csv_file()

    def _create_csv_file(self):
        with open(self.csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['item_id', 'name', 'quantity', 'issued_to_department', 'emp_id'])
            writer.writeheader()

    def load_inventory(self):
        inventory = []
        with open(self.csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['item_id'] = int(row['item_id'])
                row['quantity'] = float(row['quantity'])
                row['issued_to_department'] = row['issued_to_department'].split(';') if row['issued_to_department'] else []
                row['emp_id'] = row['emp_id'].split(';') if row['emp_id'] else []
                inventory.append(row)
        return inventory

    def save_inventory(self, inventory):
        with open(self.csv_file, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['item_id', 'name', 'quantity', 'issued_to_department', 'emp_id'])
            writer.writeheader()
            for item in inventory:
                item['issued_to_department'] = ';'.join(item['issued_to_department'])
                item['emp_id'] = ';'.join(item['emp_id'])
                writer.writerow(item)

    def get_item(self, item_id):
        inventory = self.load_inventory()
        for item in inventory:
            if item['item_id'] == item_id:
                return item
        return None

    def add_item(self, item):
        if self.get_item(item['item_id']) is not None:
            raise ValueError("Item with this ID already exists")
        inventory = self.load_inventory()
        inventory.append(item)
        self.save_inventory(inventory)

    def update_item(self, item_id, updated_item):
        inventory = self.load_inventory()
        for index, item in enumerate(inventory):
            if item['item_id'] == item_id:
                inventory[index] = updated_item
                self.save_inventory(inventory)
                return
        raise ValueError("Item with this ID does not exist.")

    def delete_item(self, item_id):
        inventory = self.load_inventory()
        inventory = [item for item in inventory if item['item_id'] != item_id]
        self.save_inventory(inventory)
