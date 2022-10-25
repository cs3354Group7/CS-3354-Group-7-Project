class Dispenser:
    def __init__(self, product = [], quantity = []):
        self.product = product
        self.quantity = quantity
        self.hasProduct = bool(self.quantity)
    
    def dispenseItem(self):
        if self.hasProduct:
            return self.quantity, self.quantity
        return [], []