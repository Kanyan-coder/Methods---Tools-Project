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

    def searchInventory(self):
        search_term = input("Enter a search term: ")
        self.cursor.execute("SELECT * FROM {} WHERE Name LIKE ?".format(self.tableName), ('%' + search_term + '%',))
        result = self.cursor.fetchall()

        if result:
            print("Search results:")
            for item in result:
                title = item[1]
                quantity = item[2]

                if quantity > 0:
                    print(f"{title} - Quantity: {quantity}")
                else:
                    print(f"{title} - Out of stock")
        else:
            print("No matching items found in the inventory.")

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

    def remQuantity(self, title, quantity):
        self.cursor.execute("UPDATE {} SET Quantity = Quantity - ? WHERE Name = ?".format(self.tableName), (quantity, title))
        self.connection.commit()

    def getQuantity(self, title):
        self.cursor.execute("SELECT Quantity FROM {} WHERE Name = ?".format(self.tableName), (title,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return 0
    def getBook(self, title):
        current_quantity = self.getQuantity(title)

        if current_quantity > 0:
            self.remQuantity(title, 1)
            self.cursor.execute("SELECT * FROM {} WHERE Name = ?".format(self.tableName), (title,))
            book = self.cursor.fetchone()
            return book
        else:
            print("Error: Book '{}' is out of stock.".format(title))
            return None
