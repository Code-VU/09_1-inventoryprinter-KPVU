stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    TotalItems = 0
    print("Inventory:")
    for item, quantity in inventory.items():
        print(quantity, item)
        TotalItems += quantity
    TotalItems=str(TotalItems)
    print("Total number of items: " + TotalItems)
if __name__ == "__main__":
    displayInventory(stuff)

#'Inventory:' in '7 rope\n12 torch\n42 gold coin\n1 ring\n12 apple\n785 axe\n'