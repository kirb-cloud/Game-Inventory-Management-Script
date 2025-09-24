#game inventory
current_inventory = {'sword':2 , 'shield':1, 'health potion':4,'gemstone':3 }
#display current inventory
print (f'current inventory: {current_inventory}')

#add new item and its quantity to inventory
new_item = (input('Enter a new item to add to inventory:'))
new_item_quantity = int(input('Enter the quantity of {new_item}:'))

# update the 'shield' item in the dictionary to 'magic shield'
current_inventory['magic shield'] = current_inventory['shield']

#gemstones to exchange for health potions
current_inventory['health potion'] += current_inventory['gemstone']

#remove gemstone from inventory
current_inventory.pop('gemstone')

#update current inventory
print(f'Updated inventory:{current_inventory}')









