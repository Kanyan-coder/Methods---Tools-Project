import sqlite3
from inventory import *

class Cart:
    
    def __init__(self, databaseName, tableName):
       
       self.databaseName = databaseName
       self.tableName = tableName
       self.cart = {}
       
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
        query = f"INSERT INTO {self.tableName} (userID, ISBN, Quantity) VALUES (?, ?, ?)"
        values = (userID, isbn, quantity_requested)
    
        self.cursor.execute(query, values)
        self.connection.commit()
        print("Item(s) have been added to your cart")
      
        
    def viewCart(self):
     
      self.cursor.execute("SELECT userID, ISBN, Quantity FROM '{}'".format(self.tableName))
      result = self.cursor.fetchall()

      if result:
        
        print("{:<15} {:<30} {:<10}".format("userID", "ISBN", "Quantity"))
        print("=" * 60)
        
        for item in result:
            
            userID, ISBN, quantity = item
            print("{:<15} {:<10} {:<10} ".format(userID, ISBN, quantity))
            print("\n")
            
      else:
        
        print("The inventory is empty.")

    def cartInfo(self):
        
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
            
               self.viewCart()
                        
            elif (choice == "2"):
                
                self.addItem()
                
            elif (choice == "3"):
                
                self.removeItem()
                
            else:
                print("Your choice was not an option. Try again.")
