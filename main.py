#main 
import sqlite3
import sys

#from inventory import *
from user import *
#from cart import *

try:
    connection = sqlite3.connect("Project.db")

    print("Successful connection")

except:
    print("Failed connection")

    sys.exit()

cursor = connection.cursor()

def login(user):
    user.login()

def logout(user):
    user.logout()

def createAccount(user):
    user.createAccount()

def main():
    #Pre-login

    user = User("Project.db", "Users")
    
    while(1):
        print("Menu Options: \n")
        print("0- Login")
        print("1- Create Account")
        print("2- Logout")
        print("3- View account information\n")
      
        opt = input("What would you like to do?\n")
        
        if(opt == "0"):
            login(user)
            print("")

        elif(opt == "1"):
            createAccount(user)
            print("")

        elif(opt == "2"):
            logout(user)
            print("")
            break

        elif(opt == "3"):
            user.viewAccountInformation()
            print("")

        else:
            print("Invalid response. Try again\n")

main()

cursor.close()
connection.close()

