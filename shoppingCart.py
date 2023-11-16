echo "class ShoppingCart:

    def __init__(self, user, inventory):
        self.user = user
        self.inventory = inventory
        self.cart = {}

    def getItems(self, ISBN):
        
        # Check if the item is in the inventory
        if self.inventory.getQuantity(ISBN) > 0:
            
            # Check if the item is already in the cart
            if ISBN in self.cart:
                
                return self.cart[ISBN]
            
            else:
                
                return 0
            
        else:
            
            print("Item not available in inventory.")
            return 0

    def removeItem(self, ISBN):
        
        if ISBN in self.cart:
            
            del self.cart[ISBN]
            print("Item removed from the cart.")
            
        else:
            
            print("Item not found in the cart.")

    def addItem(self, ISBN):
        quantity = self.getItems(ISBN)
        
        if quantity < self.inventory.getQuantity(ISBN):
            
            self.cart[ISBN] = quantity + 1
            print("Item added to the cart.")
        self.cart = cart
