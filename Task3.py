#Simple reflex agent for shopping

shoppingList = ["Bridal dress","Simple dress", "Necklace", "Flat Shoes", "Heels", "Earings" ]
global cart
def greetings():
    print("\n\nHi! Welcome to online shopping market. \n How can I help You?")
    hi = str(input("Ask Queries\t"))

#Fuction for add to cart
def add_to_cart(item, price):
    budget = int(input("Enter your budget: "))
    cart = []
    if price <= budget:
        
        cart.append(item)
        budget = budget - price
        print("Added ",item," to the cart. \nRemaining Budget: ", budget)
    else:
        print("Cannont add ",item," to cart. It exceeds budget")

#For shopping
def shopping():
    
    for item in shoppingList:
        
        if item == "Bridal dress":
            add_to_cart(item,1000)
        elif item == "Simple dress":
            add_to_cart(item, 400)
        elif item == "Necklace":
            add_to_cart(item, 2500)
        elif item == "flat shoes":
            add_to_cart(item, 300)
        elif item == "Heels":
            add_to_cart(item, 350)
        elif item == "Earings":
            add_to_cart(item, 100)
        else:
            print("Item not found in market!")

    print("Finished Shopping. \nHere is your cart:\n")
    for item in cart:
        print(item," ")

greetings()
#Calling function for shopping
shopping()
