class InventoryView:
    def display_inventory(self, inventory):
        if not inventory:
            print("No items in inventory")
            return

        print(f"{'ID':<10} {'Name':<20} {'Quantity':<10} {'Issued To Department':<30} {'Emp ID':<10}")
        print('-' * 80)

        for item in inventory:
            print(f"{item['item_id']:<10} {item['name']:<20} {item['quantity']:<10} {','.join(item['issued_to_department']):<30} {','.join(item['emp_id']):<10}")
            print('-' * 80)

    @staticmethod
    def get_item_details():
        item = {}
        item['item_id'] = input("Enter item ID: ")
        item['name'] = input("Enter item name: ")
        try:
            item['quantity'] = float(input("Enter item quantity: "))
        except ValueError:
            print("Invalid input for quantity. Please enter a numeric value.")
            return None
        item['issued_to_department'] = input("Enter issued to department (comma-separated): ").split(',')
        item['emp_id'] = input("Enter employee IDs (comma-separated): ").split(',')
        return item

    @staticmethod
    def get_item_id():
        return input("Enter item ID: ")

    @staticmethod
    def display_message(message):
        print(message)

