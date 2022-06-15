# inventory.py

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    # Prints an inventory (dictionary) 
    # Inventory:
    # 12 arrow
    # 42 gold coin
    # 1 rope
    # 6 torch
    # 1 dagger
    # Total number of items: 62

    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # Increment item total
        item_total += v

        # Print value of key and key
        print(v, k)
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    # Adds a list of items to an existing inventory (dictionary)

    for item in addedItems:
        # Adds item to dictionary with default value 0 if it does not exist
        inventory.setdefault(item, 0)

        # Increments item count
        inventory[item] += 1

# Test
displayInventory(stuff)
addToInventory(stuff, dragonLoot)
print()
displayInventory(stuff)