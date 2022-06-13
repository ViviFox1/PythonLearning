#Shopping List Maker

shoppingList = []

while True:
    #Ask for input (add to list) or nothing to move on
    print('Add an item to the list (or enter nothing to stop):')
    shoppingItem = input()

    #If nothing was entered, move on
    if(shoppingItem == ''):
        break
    
    #Add item to list
    shoppingList.append(shoppingItem)

#Output resulting list
print('You have', len(shoppingList), 'items to buy:')
for item in shoppingList:
    print(item)