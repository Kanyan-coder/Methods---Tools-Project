#main 
import sqlite3
import sys

from inventory import *
from user import *
#from cart import *

try:
    connection = sqlite3.connect("Project.db")

    print("Successful connection")

except:
    print("Failed connection")

    sys.exit()

cursor = connection.cursor()

def login(user, inv):
    user.login()
    if(user.getLoggedIn()):
        menu(user, inv)

def logout(user):
    user.logout()

def createAccount(user):
    user.createAccount()

def viewInv(inv):
    inv.showInventory()

def searchInv(inv):
    #inv.searchInventory()
    print("srch inv")

def invInfo(inv):
    while(1):
        print("Menu Options: \n")
        print("0- Go Back")
        print("1- View Inventory")
        print("2- Search Inventory\n")

        opt = input("What would you like to do?\n")

        #Go Back
        if(opt == "0"):
            break

        #View Inventory
        elif(opt == "1"):
            viewInv(inv)
            print("")

        #Search Inventory
        elif(opt == "2"):
            searchInv(inv)
            print("")

        else:
            print("Invalid response. Try again\n")


def menu(user, inv):
    while(1):
        print("Menu Options: \n")
        print("0- Logout")
        print("1- View Account Information")
        print("2- Inventory Information")
        print("3- Cart Information\n")

        opt = input("What would you like to do?\n")

        #Logout
        if(opt == "0"):
            logout(user)
            break

        #View Account Information
        elif(opt == "1"):
            user.viewAccountInformation()
            print("")

        #Inventory Information
        elif(opt == "2"):
            invInfo(inv)
            print("")

        #Cart Information
        elif(opt == "3"):
            #Adjust once cart class is added
            print("")

        else:
            print("Invalid response. Try again\n")
            




def main():
    #Pre-login

    user = User("Project.db", "Users")
    inv = Inventory("Project.db", "Inventory")
    
    while(1):
        print("Menu Options: \n")
        print("0- Login")
        print("1- Create Account")
        print("2- Exit")
      
        opt = input("What would you like to do?\n")
        
        #Login
        if(opt == "0"):
            login(user, inv)
            print("")

        #Create Account
        elif(opt == "1"):
            createAccount(user)
            print("")

        #Exit
        elif(opt == "2"):
            print("Exiting Program")
            break

        else:
            print("Invalid response. Try again\n")

main()

cursor.close()
connection.close()

