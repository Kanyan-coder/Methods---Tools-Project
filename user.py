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
    #Problem: Error if userID entered is not in database
    #Potential Fix: use conditional to confirm presence of username prior to retrieving password
    def login(self):
        userID = input("Please enter your userID... ")
        pswrd = input("Please enter your password... ")
        self.cursor.execute("SELECT Password FROM Users WHERE UserID =?", [userID])
        result = self.cursor.fetchall()
        corr = result[0][0]
        if(corr == paswrd):
            self.loggedIn = True
            print("You have logged in")
        else:
            print("There was a problem logging you in. Try again")

    #Logout function
    def logout(self):
        self.loggedIn = False

    #Function for viewing account information
    #Currently lists all UserIDs listed in database
    def viewAccountInformation(self):
        self.cursor.execute("SELECT UserID FROM Users")
        result = self.cursor.fetchall()
        for i in result:
            print(i)

    #Create Account function
    #Problem: Check to see if userID is already in use
    def createAccount(self):
        userID = input("Please enter your preferred userID...")
        pswrd = input("Please enter your preferred password...")
        name = input("Please enter your name...")
        data = (userID, pswrd, name)
        self.cursor.execute("INSERT INTO Users (UserID, Password, FirstName) VALUES (?, ?, ?)", data)
        self.connection.commit()
        print("Your account has been added")


    #Function for returning whether or not user is logged in
    def getLoggedIn(self):
        return self.loggedIn

    #Function for returning userID
    def getUserID(self):
        return self.userID

