import sqlite3

class Inventory:
    def __init__(self, project, tableName):
        self.databaseName = project
        self.tableName = tableName

        self.connection = sqlite3.connect(project)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()


    def showInventory(self):
        self.cursor.execute("SELECT ISBN, Name, Quantity, Price FROM {}".format(self.tableName))
        result = self.cursor.fetchall()

        if result:
            print("{:<15} {:<30} {:<10} {:<10}".format("ISBN", "Title", "Quantity", "Price"))
            print("=" * 65)
            for item in result:
                isbn, title, quantity, price = item
                print("{:<15} {:<30} {:<10} ${:<10}".format(isbn, title, quantity, price))
        else:
            print("The inventory is empty.")

    def searchInventory(self):
        search_term = input("Enter a search term: ")
        self.cursor.execute("SELECT ISBN, Name, Quantity, Price FROM {} WHERE Name LIKE ?".format(self.tableName), ('%' + search_term + '%',))
        result = self.cursor.fetchall()

        if result:
            print("{:<15} {:<30} {:<10} {:<10}".format("ISBN", "Title", "Quantity", "Price"))
            print("=" * 65)
            for item in result:
                isbn, title, quantity, price = item
                print("{:<15} {:<30} {:<10} ${:<10}".format(isbn, title, quantity, price))
        else:
            print("No matching items found in the inventory.")

    def addBook(self):
        isbn = int(input("Enter the ISBN of the book: "))
        title = input("Enter the title of the book: ")
        quantity = int(input("Enter the quantity of the book: "))
        price = float(input("Enter the price of the book: "))

        data = (isbn, title, quantity, price)
        self.cursor.execute("INSERT INTO {} (ISBN, Name, Quantity, Price) VALUES (?, ?, ?, ?)".format(self.tableName), data)
        self.connection.commit()
        print("Book added to inventory.")

    def remBook(self):
        title = input("Enter the title of the book to remove: ")
        self.cursor.execute("DELETE FROM {} WHERE Name = ?".format(self.tableName), (title,))
        self.connection.commit()
        print("Book removed from inventory.")

    def addQuantity(self, isbn, quantity):
        self.cursor.execute("UPDATE {} SET Quantity = Quantity + ? WHERE ISBN = ?".format(self.tableName), (quantity, isbn))
        self.connection.commit()
        print("Quantity added.")

    def remQuantity(self, isbn, quantity):
        self.cursor.execute("UPDATE {} SET Quantity = Quantity - ? WHERE ISBN = ?".format(self.tableName), (quantity, isbn))
        self.connection.commit()

    def getQuantity(self, isbn):
        self.cursor.execute("SELECT Quantity FROM {} WHERE isbn = ?".format(self.tableName), (isbn,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return 0
    
    def getPrice(self, title):
        self.cursor.execute("SELECT Price FROM {} WHERE Name = ?".format(self.tableName), (title,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

