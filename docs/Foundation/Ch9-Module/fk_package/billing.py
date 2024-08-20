class Item:
    'define the item class for representing commodities'
    def __init__(self,price):
        self.price = price
    def __repr__(self):
        return  'Item[price = %g]' %self.price

def test():
    goods = Item(500)
    print(goods.__repr__())

__all__ = ['Item']

if __name__ == '__main__':
    test()