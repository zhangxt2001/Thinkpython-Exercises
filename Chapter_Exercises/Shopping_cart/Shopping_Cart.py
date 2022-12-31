from Item import Item

class ShoppingBasket:
    def __init__(self):
        self.items = {} #This is a dictionary in the form {item:quantity}
    
    def addItem(self,Item,quantity):
        '''
Adding an item to the shopping basket.
Instance method
'''
        if quantity <= 0:
            raise ValueError("Please enter a valid quantity")
        if Item.name in self.items:
            self.items[Item] += quantity
        else:
            self.items[Item] = quantity
    
    def RemoveItem(self,Item,quantity):
        '''
Removing specified quantity of an Item from the shopping cart
Instance method
'''
        if quantity < 0:
            raise ValueError("Please enter a valid quantity")
        new_quantity = self.items[Item] - quantity
        if new_quantity <= 0:
            self.items.pop(Item)
        else:
            self.items[Item] = new_quantity
            
    
    def UpdateQuantity(self,Item,new_quantity):
        '''
Updating the desired quantity of an item from the shopping basket
Instance method
'''
        if new_quantity < 0:
            raise ValueError("Please enter a valid new quantity")
        elif new_quantity == 0:
            self.items.pop(Item)
        else:
            self.items[Item] = new_quantity
    
    def ViewContent(self):
        '''
Viewing/listing the content of the shopping basket
Instance method
'''
        return_list = []
        for key in self.items:
            return_list.append(key.name)
        return return_list
    
    def TotalCost(self):
        '''
Calculating the total cost of the shopping basket
Instance method
'''
        total_cost = 0
        for key in self.items:
            total_cost += key.price*self.items[key]
        return total_cost
     
    def Reset(self):
        '''
Emptying/Resetting the shopping basket
Instance method
'''
        self.items = {}
    
    def IfEmpty(self):
        '''
Checking if the shopping basket is empty, if empty return
True
Instance method
'''
        return len(list(self.items.keys())) == 0