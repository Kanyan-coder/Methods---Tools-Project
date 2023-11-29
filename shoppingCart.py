import sqlite3
from inventory import *

class Cart:
    
    def __init__(self, databaseName, tableName):
       
       self.databaseName = databaseName
       self.tableName = tableName
       #self.cart = {}
       
       self.connection = sqlite3.connect(databaseName)
       self.cursor = self.connection.cursor()
    
    def __del__(self):
        
        self.cursor.close()
        self.connection.close()

    def getItems(self, ISBN):
       
        if self.inventory.getQuantity(ISBN) > 0:
           
            if ISBN in self.cart:
                
                return self.cart[ISBN]
            
            else:
                
                return 0
            
        else:
            
            print("Item not available in inventory.")
            
            return 0

    def removeItem(self):
        
        ISBN = input("What is the ISBN number of the book you would like to remove?\n")
        if ISBN in self.cart:
            
            del self.cart[ISBN]
            print("\nItem was removed from the cart.\n")
            
        else:
            
            print("\nItem was not found in the cart.\n")
    
    def addToCart(self, userID, isbn, quantity_requested):
        data = (userID, isbn, quantity_requested)
        self.cursor.execute("INSERT INTO '{}' (UserID, ISBN, Quantity) VALUES (?, ?, ?)".format(self.tableName), data)
        self.connection.commit()
        print("Item(s) have been added to your cart")

    def viewCart(self):
        
        while(1):
             
            print("Menu Options: \n")
            print("0- Back")
            print("1- View Cart")
            print("2- Add To Cart")
            print("3- Remove From Cart\n")

            choice = input("What would you like to do?\n")

            if (choice == "0"):
                
                break

            elif(choice == "1"):
            
                if not self.cart:
            
                    print("Cart is empty.\n")
            
                else:
            
                    print("Shopping Cart Contents:")
                    for ISBN, quantity in self.cart.items():
                
                        print(f"ISBN: {ISBN}, Quantity: {quantity}")
                        
            elif (choice == "2"):
                
                self.addItem()
                
            elif (choice == "3"):
                
                self.removeItem()
                
            else:
                print("Your choice was not an option. Try again.")
