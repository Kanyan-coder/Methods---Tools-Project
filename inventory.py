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
        self.cursor.execute("SELECT Name, Quantity, Price FROM {}".format(self.tableName))
        result = self.cursor.fetchall()

        if result:
            print("{:<30} {:<10} {:<10}".format("Title", "Quantity", "Price"))
            print("=" * 50)
            for item in result:
                title, quantity, price = item
                print("{:<30} {:<10} ${:<10}".format(title, quantity, price))
        else:
            print("The inventory is empty.")

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
    
    def getPrice(self, title):
        self.cursor.execute("SELECT Price FROM {} WHERE Name = ?".format(self.tableName), (title,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        else:
            return None

    def getBook(self, title):
        current_quantity = self.getQuantity(title)

        if current_quantity > 0:
            self.remQuantity(title, 1)
            price = self.getPrice(title)

            if price is not None:
                print("Book '{}' obtained. Price: ${}".format(title, price))
                self.cursor.execute("SELECT * FROM {} WHERE Name = ?".format(self.tableName), (title,))
                book = self.cursor.fetchone()
                return book, price
            else:
                print("Error: Price not found for book '{}'.".format(title))
                return None
        else:
            print("Error: Book '{}' is out of stock.".format(title))
            return None
def main():
    inventory_sys = Inventory("Project.db", "Inventory")

    while True:
        print("\n===== Inventory Management Menu =====")
        print("1. Show Inventory")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Add Quantity")
        print("5. Search Inventory")
        print("6. Get Book Details with Price")
        print("0. Exit")

        choice = input("Enter your choice (0-6): ")
        if choice == "0":
            break
        elif choice == "1":
            inventory_sys.showInventory()
        elif choice == "2":
            inventory_sys.addBook()
        elif choice == "3":
            inventory_sys.remBook()
        elif choice == "4":
            inventory_sys.addQuantity()
        elif choice == "5":
            inventory_sys.searchInventory()
        elif choice == "6":
            book_title = input("Enter the title of the book to get details: ")
            book_info = inventory_sys.getBook(book_title)
if __name__ == "__main__":
    main()
