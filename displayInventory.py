stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    TotalItems = 0
    for item, quantity in inventory.items():
        print(quantity, item)
        TotalItems += quantity
    print("Total number of items: {TotalItems}")
if __name__ == "__main__":
    displayInventory(stuff)
