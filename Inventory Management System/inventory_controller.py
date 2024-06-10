def __init__(self, model, view):
    self.model = model
    self.view = view


def list_items(self):
    inventory = self.model.load_inventory()
    self.view.display_inventory(inventory)


def add_item(self):
    item = self.view.get_item_details()
    if item:
        try:
            self.model.add_item(item)
            self.view.display_message("Item added successfully.")
        except ValueError as e:
            self.view.display_message(str(e))


def update_item(self):
    item_id = self.view.get_item_id()
    if not item_id:
        self.view.display_message("Item ID cannot be empty.")
        return
    updated_item = self.view.get_item_details()
    if updated_item:
        try:
            self.model.update_item(item_id, updated_item)
            self.view.display_message("Item updated successfully.")
        except ValueError as e:
            self.view.display_message(str(e))


def delete_item(self):
    item_id = self.view.get_item_id()
    if not item_id:
        self.view.display_message("Item ID cannot be empty.")
        return
    try:
        self.model.delete_item(item_id)
        self.view.display_message("Item deleted successfully.")
    except ValueError as e:
        self.view.display_message(str(e))


def get_item(self):
    item_id = self.view.get_item_id()
    if not item_id:
        self.view.display_message("Item ID cannot be empty.")
        return
    item = self.model.get_item(item_id)
    if item:
        self.view.display_inventory([item])
    else:
        self.view.display_message("Item not found.")