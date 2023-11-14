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
        self.cursor.execute("SELECT * FROM {}".format(self.tableName))
        result = self.cursor.fetchall()
        for Title in result:
            print(Title)

    def addBook(self):
        isbn = int(input("Enter the ISBN of the book: "))
        title = input("Enter the title of the book: ")
        quantity = int(input("Enter the quantity of the book: "))

        data = (isbn, title, quantity)
        self.cursor.execute("INSERT INTO {} (ISBN, Name, Quantity) VALUES (?, ?, ?)".format(self.tableName), data)
        self.connection.commit()
        print("Book added to inventory.")

    def remBook(self):
        title = input("Enter the title of the book to remove: ")
        self.cursor.execute("DELETE FROM {} WHERE Name = ?".format(self.tableName), (title,))
        self.connection.commit()
        print("Book removed from inventory.")

    def addQuantity(self):
        title = input("Enter the title of the book to add quantity: ")
        quantity = int(input("Enter the quantity to add: "))
        self.cursor.execute("UPDATE {} SET Quantity = Quantity + ? WHERE Name = ?".format(self.tableName), (quantity, title))
        self.connection.commit()
        print("Quantity added.")

    def remQuantity(self):
        title = input("Enter the title of the book to remove quantity: ")
        quantity = int(input("Enter the quantity to remove: "))
        self.cursor.execute("UPDATE {} SET Quantity = Quantity - ? WHERE Name = ?".format(self.tableName), (quantity, title))
        self.connection.commit()
        print("Quantity removed.")

    def getQuantity(self, title):
        self.cursor.execute("SELECT Quantity FROM {} WHERE Name = ?".format(self.tableName), (title,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return 0
    def getBookLocation(self, title):
        self.cursor.execute("SELECT rowid FROM {} WHERE Name = ?".format(self.tableName), (title,))
        result = self.cursor.fetchone()

        if result:
            return result[0]
        else:
            print("Book not found in inventory.")
            return None
        
