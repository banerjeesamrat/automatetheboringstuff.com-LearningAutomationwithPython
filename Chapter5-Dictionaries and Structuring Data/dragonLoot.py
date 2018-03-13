"""
Imagine that a vanquished dragon’s loot is represented as a list of strings like
this:


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

Write a function named addToInventory(inventory, addedItems), where the
inventory parameter is a dictionary representing the player’s inventory
(like in the previous project) and the addedItems parameter is a list like
dragonLoot. The addToInventory() function should return a dictionary that
represents the updated inventory. Note that the addedItems list can contain
multiples of the same item. Your code could look something like this:


def addToInventory(inventory, addedItems):
    # your code goes here

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
The previous program (with your displayInventory() function from the previous project) would output the following:


Inventory:
45 gold coin
1 rope
1 ruby
1 dagger

Total number of items: 48

"""

inv = {'gold coin': 42, 'rope': 1}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def addToInventory(inventory, addItems):
    for k in range(len(addItems)):
        if addItems[k] in inventory.keys():
            inventory[addItems[k]] += 1
        else:
            inventory.setdefault(addItems[k], 1)
    return inventory



def displayInventory(inv):
    print("Inventory:")
    item_total = 0
    for k, v in inv.items():        
        print(str(v)+ ' '+str(k))
        item_total=item_total+inv.get(k,0)
    print("Total number of items: " + str(item_total))



inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
