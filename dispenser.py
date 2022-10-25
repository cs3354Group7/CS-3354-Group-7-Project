class Dispenser:
    def __init__(self, products = {}):
        self.product = products # Stores a product dictionary where the key is the product name 
                                # and the value if the product quantity.
        self.hasProduct = bool(self.product)
    
    def dispenseItems(self):
        if self.hasProduct:
            return self.product
        return {}
    
    def addItems(self, item = {}):
        try: 
            self.product.update(item) # Merge existing products with new products
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            return "Error adding item"