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

def viewInv(inv):
    inv.showInventory()

def searchInv(inv):
    inv.searchInventory()
    print("srch inv")
    
def viewCart(cart):
    cart.viewCart()
    
def addItem(cart):
    cart.addItem()    
    

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
            print("")
            print("0- Go Back")
            print("1- Buy Books\n")
            
            choice = input("What would you like to do?\n")

            if(choice == "0"): 
                break;
            
            #if user is buying a book
            elif(choice == "1"):

               inventory = Inventory("Project.db", "Inventory")
               shopping_cart = Cart("Project.db", 'Shopping Cart')
               book_details = inventory.getBook()
               
               if book_details:
                    isbn, title, quantity, price = book_details
                    shopping_cart.addItem(isbn, title, quantity, price)
                    
               inventory.conn.commit()
               shopping_cart.conn.commit()
                
                   
            else:
                print("invalid choice. Try again.")

        #Search Inventory
        elif(opt == "2"):
            inv.searchInventory()
            print("")

        else:
            print("Invalid response. Try again\n")


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
            invInfo(inv)
            print("")

        #Cart Information
        elif(opt == "3"):
            cart.viewCart()
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

