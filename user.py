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
    #Information could be more organized
    def viewAccountInformation(self):
        if(self.loggedIn):
            self.cursor.execute("SELECT * FROM Users WHERE UserID =?", [self.userID])
            result = self.cursor.fetchall()
            for i in result:
                print(i)
        else:
            print("\nTry logging in first")

    #Create Account function
    #Make sure to adjust when full user table is complete
    def createAccount(self):
        userID = input("Please enter your preferred userID...")
        self.cursor.execute("SELECT COUNT(UserID) FROM Users WHERE UserID =?", [userID])
        result = self.cursor.fetchall()
        numUsrs = result[0][0]
        if(numUsrs == 0):
            pswrd = input("Please enter your preferred password...")
            name = input("Please enter your name...")
            data = (userID, pswrd, name)
            self.cursor.execute("INSERT INTO Users (UserID, Password, FirstName) VALUES (?, ?, ?)", data)
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

