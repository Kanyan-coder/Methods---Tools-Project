#User Class
import sqlite3

class User:
    #Constructor
    def __init__(self, databaseName, tableName, loggedIn = False, userID = ""):
        self.databaseName = databaseName
        self.tableName = tableName
        self.loggedIn = loggedIn
        self.userID = userID

        self.connection = sqlite3.connect(databaseName)
        self.cursor = self.connection.cursor()
    
    #Destructor
    def __del__(self):
        self.cursor.close()
        self.connection.close()

    #Login function
    def login(self):
        userID = input("Please enter your userID... ")
        self.cursor.execute("SELECT COUNT(UserID) FROM Users WHERE UserID =?", [userID])
        result = self.cursor.fetchall()
        numUsrs = result[0][0]
        if(numUsrs != 0):
            pswrd = input("Please enter your password... ")
            self.cursor.execute("SELECT Password FROM Users WHERE UserID =?", [userID])
            result = self.cursor.fetchall()
            corr = result[0][0]
            if(corr == pswrd):
                self.loggedIn = True
                self.userID = userID
                print("\nYou have logged in")
            else:
                print("\nThere was a problem logging you in. Try again")
        else:
            print("\nUsername not found. Try again")
        return self.loggedIn

    #Logout function
    def logout(self):
        self.userID = ""
        self.loggedIn = False
        return self.loggedIn

    #Function for viewing account information
    def viewAccountInformation(self):
        if(self.loggedIn):
            self.cursor.execute("SELECT * FROM Users WHERE UserID =?", [self.userID])
            result = self.cursor.fetchall()
            print("UserID: ", result[0][0])
            print("Email: ", result[0][1])
            print("Password: ", result[0][2])
            print("First Name: ", result[0][3])
            print("Last Name: ", result[0][4])
            print("Address: ", result[0][5])
            print("City: ", result[0][6])
            print("State: ", result[0][7])
            print("Zipcode: ", result[0][8])
            print("Payment: ", result[0][9])
        else:
            print("\nTry logging in first")

    #Create Account function
    def createAccount(self):
        userID = input("Please enter your preferred userID...")
        self.cursor.execute("SELECT COUNT(UserID) FROM Users WHERE UserID =?", [userID])
        result = self.cursor.fetchall()
        numUsrs = result[0][0]
        if(numUsrs == 0):
            pswrd = input("Please enter your preferred password...")
            email = input("Please enter your email...")
            frstName = input("Please enter your first name...")
            lstName = input("Please enter your last name...")
            addr = input("Please enter your street address (ex: 123 Elm Rd)...")
            city = input("Please enter the city you are from...")
            state = input("Please enter the state you are from (ex: MS)...")
            zipCde = input("Please enter the your zipcode...")
            pymnt = input("Please enter your payment method (ex: Visa, Mastercard, American Express)...")
            data = (userID, email, pswrd, frstName, lstName, addr, city, state, zipCde, pymnt)
            self.cursor.execute("INSERT INTO Users (UserID, Email, Password, FirstName, LastName, Address, City, State, Zipcode, Payment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
            self.connection.commit()
            print("\nYour account has been added")
        else:
            print("\nUserID already in use. Please try another")


    #Function for returning whether or not user is logged in
    def getLoggedIn(self):
        return self.loggedIn

    #Function for returning userID
    def getUserID(self):
        return self.userID

