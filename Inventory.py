class Inventory:
    def __init__(self, inventory = {}):
        self.inventory = inventory
    
    def get_Quantity(self, item):
        value = self.inventory.get(item)
        if (value == None):
            return 0
        else:
         return value 
        
    def add(self, item):
        count = self.inventory.get(item)
        self.inventory[item] = count + 1
    
    def sub(self, item):
        if(bool(self.inventory[item])):
            count = self.inventory.get(item)
            self.inventory[item] = count - 1
           
    
    def clear_Item(self, item):
        self.inventory.pop(item)
        
    
    def put(self, item, qty):
        self.inventory[item] = qty
        
        
    def print_Item(self, item):
        print(item + " " + repr(self.inventory[item]))
