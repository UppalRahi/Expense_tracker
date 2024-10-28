# print("Welcome to the cafe\n Coffee = Rs10\n Tea = Rs5\n Water = Rs2\n Juice = Rs15")
import time
menu = {
    "pizza": 40,"pasta": 60,"burger": 60,"sandwich": 10,"salad":30
}
#Greet 
print("Welcome to python cafe")
print("pizza: 40\npasta: 60\nburger: 60\nsandwich: 10\nsalad: 30")

order_total = 0

item_1 = input("What would you like to order? ")
item_2 = input("What else would you like to order? ")
if (item_1 in menu):
    order_total += menu[item_1]
    if (item_2 in menu):
        order_total += menu[item_2]
    elif (item_2 == "no"):
        pass
    else:
        print("Sorry, we don't have that item")
        time.sleep(5)
else:
    print("Sorry, we don't have that item")
print("Your total is: ", order_total)