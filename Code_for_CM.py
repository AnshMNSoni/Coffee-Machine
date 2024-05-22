# Day :: 15

# Coffee Machine:

from rich.console import Console
import time
from Coffee import logo

Price_tag = {
    'espresso': 10,
    'latte': 20,
    'cappuccino': 30
}

available = {
            'Water': 1000,
            'coffee': 100,
            'Milk': 500
        } 

requirements = {
        'espresso': [50, 18, 0],
        'latte': [200, 24, 150],
        'cappuccino': [250, 24, 100]
}

def clearall():
    console = Console()
    console.clear()
 
# For report:   
def non_user(argument):        
    for item in available:
        if (item == 'Water' or item == 'Milk'):
            print(f"{item} : {available[item]} ml")
        else:
            print(f"{item} : {available[item]} g")
        
    Coffee_Machine()
    
# Main Function:    
def Coffee_Machine():
    like = input("What would you like? (espresso / latte / cappuccino): ")
    
    # to trace the ingrediants
    if (like == 'report'):
        non_user(like)
    
    price_tag = """
Price Tag:
espresso -> $10
latte -> $20
cappuccino -> $30
"""
    print(price_tag)
    
    pay = int(input("Please insert your money here (Change will be provided if necessary): "))
    
    # if pay is sufficient or more than the require amount
    if (pay >= Price_tag[like]):
        
        # List of elements in available
        lst1 = list(dict.values(available))
        
        # List of elements in requirements
        lst2 = requirements[like]
        
        
        lst = []
        for i in range(0, 3):
            if (lst1[i] >= lst2[i]):
                add = lst1[i] - lst2[i]
                lst.append(add)
                continue
            
            # If atleast one of element in requirements is less than elements in available
            else:
                print(f"Sorry! ingrediants not enough to make {like}.")
                print(f"Hence, your ${pay} is Refunded.\n")
                
                play_again = input("Want to play Again? Type 'y' or 'n': ")
                if (play_again == 'y'):
                    clearall()
                    print(logo)
                    Coffee_Machine()
                else:
                    break
                
        # Refining the available dictonary
        i = 0
        for item in available:
            available[item] = lst[i]
            i += 1

        # if payment is more then change will be provided
        change = pay - Price_tag[like]
        
        if (change == 0):
            for Time in range(7, 0, -1):
                clearall()
                print(logo)
                print(f"Enjoy your ☕ {like}.")
                print(f"Next Coffee in {Time} sec...")
                time.sleep(1)
            
            clearall()
            print(logo)
            Coffee_Machine()
            
        else:
            for Time in range(7, 0, -1):
                clearall()
                print(logo)
                print(f"Your Change = ${change}")
                print(f"Enjoy your ☕ {like}.")
                print(f"Next Coffee in {Time} sec...")
                time.sleep(1)
            
            clearall()
            print(logo)
            Coffee_Machine()
    
    # if pay is less than the require amount          
    else:
        print(f"Sorry! Price for {like} is {Price_tag[like]}")
        print(f"Hence, your ${pay} is Refunded.\n")
        
        play_again = input("Want to play Again? Type 'y' or 'n': ")
        if (play_again == 'y'):
            clearall()
            print(logo)
            Coffee_Machine()
        else:
            clearall()
            print("Visit Again!")
    
    

# Starting of the Code:
clearall()
print(logo)
Coffee_Machine()                