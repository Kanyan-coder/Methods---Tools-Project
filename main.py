#main 
from functools import cached_property
import sqlite3
import sys

from inventory import *
from user import *
from shoppingCart import *

try:
    connection = sqlite3.connect("Project.db")

    print("Successful connection")

except:
    print("Failed connection")

    sys.exit()

cursor = connection.cursor()

def login(user, inv, cart):
    user.login()
    if(user.getLoggedIn()):
        menu(user, inv, cart)

def logout(user):
    user.logout()

def createAccount(user):
    user.createAccount()

def viewInv(user, inv, cart):
    while(1):
        inv.showInventory()
        print("")
        print("")
        print("0- Go Back")
        print("1- Add a Book to Your Cart\n")
        
        opt = input("What would you like to do?\n")

        if(opt == "0"): 
            break
        
        #if user is buying a book
        elif(opt == "1"):
            addItem(user, inv, cart)
            
        else:
            print("invalid choice. Try again.")


def searchInv(inv):
    inv.searchInventory()
    
    
def addItem(user, inv, cart):
    isbn = int(input("Enter the ISBN of the book you'd like to add: "))
    qnt = int(input("Enter desired quantity: "))
            
    if(inv.getQuantity(isbn) == 0):
        print("Cannot find book in stock")

    else:
        while(1): 
            if(qnt == 0):
                break

            elif(inv.getQuantity(isbn) >= qnt):
                cart.addToCart(user.getUserID(), isbn, qnt)
                inv.remQuantity(isbn, qnt)
                break

            else:
                print("Not enough in stock")
                qnt = int(input("Enter desired quantity or 0 to go back: "))

        print("")
    

def invInfo(user, inv, cart):
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
            viewInv(user, inv, cart)
            
        #Search Inventory
        elif(opt == "2"):
            inv.searchInventory()
            print("")

        else:
            print("Invalid response. Try again\n")
            
def cartInfo(user, inv, cart):
        
        while(1):
             
            print("Menu Options: \n")
            print("0- Back")
            print("1- View Cart")
            print("2- Add To Cart")
            print("3- Remove From Cart")
            print("4- Check Out\n")

            choice = input("What would you like to do?\n")

            if (choice == "0"):
                
                break

            elif(choice == "1"):
            
               cart.viewCart(user.getUserID())
                        
            elif (choice == "2"):
                
                addItem(user, inv, cart)
                
            elif (choice == "3"):
                
                cart.removeItem(inv, user.getUserID())

            elif (choice == "4"):
                cart.checkOut(inv, user.getUserID())
                
            else:
                print("Your choice was not an option. Try again.")


def menu(user, inv, cart):
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
            invInfo(user, inv, cart)
            print("")

        #Cart Information
        elif(opt == "3"):
            cartInfo(user, inv, cart)
            #print("")

        else:
            print("Invalid response. Try again\n")
            




def main():
    #Pre-login

    user = User("Project.db", "Users")
    inv = Inventory("Project.db", "Inventory")
    cart = Cart("Project.db", "Shopping Cart")
    
    while(1):
        print("Menu Options: \n")
        print("0- Login")
        print("1- Create Account")
        print("2- Exit")
      
        opt = input("What would you like to do?\n")
        
        #Login
        if(opt == "0"):
            login(user, inv,cart)
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

