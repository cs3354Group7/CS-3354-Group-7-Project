'''
The Inventory class stores all the items within a vending machine. 
The items include the item name and the item quantity. The get_Quantity
function returns the quantiy of a selected item. The item quantity is able
to be added to and subtracted using the sub and add functions. 
'''

class Inventory:
    def __init__(self, inventory = {}):
        self.inventory = inventory
        
    def get_Price(self, item):
        return self.inventory.get(item).getPrice()
    
    def get_Quantity(self, item):
        value = self.inventory.get(item).getQuantity()
        if (value == None):
            return 0
        else:
         return value 
        
    def get_Item(self, item):
        return self.inventory.get(item)

    def add(self, item):
        count = self.inventory.get(item)
        self.inventory[item] = count + 1
    
    def sub(self, item):
        if(bool(self.inventory[item])):
            count = self.inventory.get(item)
            if((count - 1) >= 0):
                self.inventory[item] = count - 1
           
    
    def clear_Item(self, item):
        self.inventory.pop(item)
        
    
    def put(self, item, qty):
        self.inventory[item] = qty
        
        
    def print_Item(self, item):
        print(item + " " + repr(self.inventory[item]))
