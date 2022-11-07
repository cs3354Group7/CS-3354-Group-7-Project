'''
The coin collector class holds all the information
relating to the coin level of a vending machine. The maximum
amount of coins in the vending machine is 1000 coins. The collector
stores the amount of coins, and whether the collector is full or not.
The addCoins function lets a certain number of coins be added to
the coin count. The getCoins funcion returns the number of coins in
the collector. 
'''

class CoinCollector:
    def init(self, isFull, isEmpty, coinCount, max):
        self.coinCount = coinCount
        self.max = 1000
        self.isFull = bool(self.coinCount == self.max)
        self.isEmpty = bool(self.coinCount)

    # checking to see if coins in machine are empty or full
    def isEmpty(self):
        return self.isEmpty

    def isFull(self):
        return self.isFull

    # add coins
    def addCoins(self, n):
        if self.coinCount + n <= self.max:
            self.coinCount += n

    # return number of coins
    def getCoins(self):
        return self.coinCount
