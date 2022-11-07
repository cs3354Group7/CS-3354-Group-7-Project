'''
The Dispenser class is responsible for checking 
dispensing items to the user. It stores which items the user
wants to dispense and the quantity of each item. The dispenseItems
function returns all the items currently in the dispenser.
The addItems function adds new items to the items that already 
exist in the dispenser. 
'''

class Dispenser:
    def __init__(self, products = {}):
        self.product = products # Stores a product dictionary where the key is the product name 
                                # and the value if the product quantity.
        self.hasProduct = bool(self.product)
    
    # Returns the items in the dispenser and resets
    # the amount of products in the dispenser
    def dispenseItems(self):
        if self.hasProduct:
            products = self.product
            self.product = {}
            return products
        return {}
    
    def addItems(self, item = {}):
        try: 
            self.product.update(item) # Merge existing products with new products
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            return "Error adding item"
