class Item:
    def __init__(self, price, id, name, quantity):
	self.price = price
	self.id = id
	self.name = name
	self.quantity = quantity
    
    #getter and setter function for price
    def setPrice(self, p):
        self.price = p
		
    def getPrice(self):
        return self.price	
		
	  #getter and setter function for id
    def setID(self, i):
        self.id = i
		
    def getID(self):
        return self.id	
		
	  #getter and setter function for name
    def setName(self, n):
        self.name = n
		
    def getName(self):
        return self.name
	
	  #getter and setter function for quantity
    def setQuantity(self, q):
        self.quantity = q
		
    def getQuantity(self):
        return self.quantity
	
