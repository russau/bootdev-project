def create_inventory_menu(inventory):
    inventory_menu = [ 
        f"({i}) {item}" for i, item in enumerate(inventory, start=1)
    ]

    return inventory_menu
