import sqlite3
from inventory import *
from user import *

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

    def checkOut(self, inv, userID):
        self.cursor.execute("SELECT COUNT(ISBN) FROM '{}' WHERE userID = ?".format(self.tableName), (userID,))
        result = self.cursor.fetchall()
        cnt = result[0][0]
        
        self.cursor.execute("SELECT ISBN, Quantity FROM '{}' WHERE userID = ?".format(self.tableName), (userID,))
        result = self.cursor.fetchall()
        
        print("{:<30} {:<30} {:<30}".format("Title", "Quantity", "Price"))
        print("=" * 90)
        
        total = 0
        
        for i in range(cnt):
            isbn = result[i][0]
            qnt = result[i][1]
            book = inv.getBook(isbn)
            price = qnt * book[0][2]
            total += price
            print("{:<30} {:<30} {:<30} ".format(book[0][1], qnt,"%.2f"% price))
            
        total = "{:.2f}".format(total)
        print("\nTotal: $", total)
        print("\n")

        self.cursor.execute("DELETE FROM '{}' WHERE userID = ?".format(self.tableName), (userID,))
        self.connection.commit()
            
            
        
        
  
        
    def removeItem(self, inv, userID):
         
        isbn = input("Enter the ISBN of the book to remove: ")
        
        

        self.cursor.execute("SELECT * FROM '{}' WHERE userID = ? AND ISBN = ?".format(self.tableName), (userID,isbn,))
        result = self.cursor.fetchone()
        
        if result:
            
            self.cursor.execute("UPDATE '{}' SET Quantity = Quantity - 1 WHERE userID = ? AND ISBN = ? AND Quantity > 0".format(self.tableName), (userID,isbn,))
            self.connection.commit()
            print("\nItem was removed from Cart.\n")
            inv.addQuantity(isbn, 1)
            
        else:
            
            print("\nItem was not found in the cart.\n")
    
    def addToCart(self, userID, isbn, quantity_requested):
        self.cursor.execute("SELECT COUNT(userID) FROM '{}' WHERE userID = ? AND ISBN = ?".format(self.tableName), (userID,isbn,))
        result = self.cursor.fetchone()
        
        if(result[0] == 0):
            data = (userID, isbn, quantity_requested)
            self.cursor.execute("INSERT INTO '{}' (UserID, ISBN, Quantity) VALUES (?, ?, ?)".format(self.tableName), data)
            
        else:
            data = (quantity_requested, userID, isbn)
            self.cursor.execute("UPDATE '{}' SET Quantity = Quantity + ? WHERE userID = ? AND ISBN = ? AND Quantity > 0".format(self.tableName), (data))
            
        self.connection.commit()
        print("Item(s) have been added to your cart")
      
        
    def viewCart(self,userID):
      
      self.cursor.execute("SELECT userID, ISBN, Quantity FROM '{}' WHERE userID = ?".format(self.tableName), (userID,))
      result = self.cursor.fetchall()

      if result:
        
        print("{:<15} {:<30} {:<10}".format("userID", "ISBN", "Quantity"))
        print("=" * 60)
        
        for item in result:
            
            userID, ISBN, quantity = item
            print("{:<15} {:<30} {:<10} ".format(userID, ISBN, quantity))
            print("\n")
            
      else:
        
        print("The inventory is empty.")

    
