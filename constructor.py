# Constructor is the method that is initialized as soon as object 
#of a class is instantiated.

class Item:
    def __init__(self ,name : str , price , quantity = 0 ):
        
        assert isinstance(name , str) , f"{name} is not of string Type"
        assert price > 0 , "Sorry price should be greater than zero!"
        
        #assigning each instance 
        self.name = name
        self.price = price 
        self.quantity = quantity
        
    def __str__(self):
        return f"Item object is {self.name} with price {self.price} and a number of {self.quantity} items! "
        

item1 = Item("Phone" , 750 , 10 )
item2 = Item("Laptop", 1200 , 20)
item3 = Item("TV" , 800 )

print(item1)