# Name: Vivian Yang
# Date: Mar 29, 2023
# Desc: This program allows the customer to select cakes and the quantity they wish to purchase and then outputs the amount the customer owes.
# -----------------------------------------------------------------------------------------------------------------------------------------------

menu = "Cake Menu".center(36) # this function centers "Cake Menu" below the cake emoji.
print("Welcome to Vivian's Cake Shop!\n") 

print("╭──── ⋅ ⋅ ⋅ ──── 🍰 ──── ⋅ ⋅ ⋅ ────╮\n"
      "\n\n", menu, "\n"
      "\n1. Decadent Chocolate      $12.99"
      "\n2. Rich Red Velvet         $15.99"
      "\n3. Classic Crepe           $50.99"
      "\n4. Velvety Vanilla         $11.59"
      "\n5. Creamy Cheesecake       $23.99\n\n"
      "\n╰──── ⋅ ⋅ ⋅ ────  .  ──── ⋅ ⋅ ⋅ ────╯\n")
# the above code prints the welcome message and the menu


item = int(input("What item would you like to purchase?(Enter the number): ")) # asks the user what they want to buy and casts it into an integer value for the following if statments
if item == 1: # i.e. if user enters 1, sets variable "cake" to Decadent Chocolate and cakePrice to 12.99
    cake = "Decadent Chocolate"
    cakePrice = 12.99
elif item == 2: 
    cake = "Rich Red Velvet"
    cakePrice = 15.99
elif item == 3: 
    cake = "Classic Crepe"
    cakePrice = 50.99
elif item == 4: 
    cake = "Velvety Vanilla"
    cakePrice = 11.59
elif item == 5: 
    cake = "Creamy Cheesecake"
    cakePrice = 23.99
else: # if all of the above is false, it prints the following:
    print("Sorry, that item isn't on the menu.")
    
amount = int(input("How many do you want? ")) # asks user how many they want

more = input("Do you want to purchase another item?(y/n): ") # asks user if they want to purchase another item
if more == "y" or more == "Y": # if user enters y or Y
    item2 = int(input("What other item would you like to purchase?(Enter the number): ")) # asks user what other item they'd like to purchase
    if item2 == 1: # i.e. if user enters 1, sets variables cake2 to Decadent Chocolate and cake2Price to 12.99
        cake2 = "Decadent Chocolate"
        cake2Price = 12.99
    elif item2 == 2: 
        cake2 = "Rich Red Velvet"
        cake2Price = 15.99
    elif item2 == 3: 
        cake2 = "Classic Crepe"
        cake2Price = 50.99
    elif item2 == 4: 
        cake2 = "Velvety Vanilla"
        cake2Price = 11.59
    elif item2 == 5:
        cake2 = "Creamy Cheesecake"
        cake2Price = 23.99
    else: # if all of the above is false, it prints the following:
        print("Sorry, that item isn't on the menu.")
        
    amount2 = int(input("How many do you want? ")) # asks user how many they want
        
    print("\nYour order:\n" + str(amount) + "x", cake) # prints "Your order" on a separate line from the first item the user ordered
    print(str(amount2) + "x", cake2) # prints the amount and name of the second item

    # the following code calculates the subtotal, tax, and total
    subtotal = round(cakePrice*amount + cake2Price + amount2, 2) # the round function rounds the float to 2 decimal places
    tax = round(subtotal*0.13, 2)
    total = round(subtotal+tax, 2)
    totals = "\nSubtotal: $" + str(subtotal)+ "\nTax: $" + str(tax) + "\nTotal: $" + str(total)
    
    if item2 == 1: # depending on the user input, the totals that are printed will change
        print(totals)
    elif item2 == 2:
        print(totals)
    elif item2 == 3:
        print(totals)
    elif item2 == 4:
        print(totals)
    elif item2 == 5:
        print(totals)
    else:
        print("Sorry, that item is not on the menu.")


elif more == "n" or more == "N": # if the user enters n or N, the following code will be printed
    print("\nYour order:\n" + str(amount) + "x", cake)
    subtotal = round(cakePrice*amount, 2) 
    tax = round(subtotal*0.13, 2)
    total = round(subtotal+tax, 2)
    totals = "\nSubtotal: $" + str(subtotal)+ "\nTax: $" + str(tax) + "\nTotal: $" + str(total)
    if item == 1: # depending on the user input, the totals that are printed will change
        print(totals)
    elif item == 2:
        print(totals)
    elif item == 3:
        print(totals)
    elif item == 4:
        print(totals)
    elif item == 5:
        print(totals)
    else:
        print("Sorry, that item is not on the menu.")


# the following code is the code for the payment
payment = float(input("\nEnter the amount of your payment: $")) # asks user for payment
change = round(payment-total, 2) # rounds change to 2 decimal places
if payment < total: # if the payment isn't enough, it asks the user to try again
    print("Not enough payment, please try again.")
    payment2 = float(input("\nEnter the amount of your payment: $"))
    change2 = round(payment2-total, 2)
if payment >= total: # if the payment is enough, it will give the user change and say bye
    print("Transaction approved! Your change is $%.2f" % change) # outputs the change with 2 decimal places
    print("\nThanks for dining at Vivian's Cake Shop! See you again soon :)!")
elif payment2 >= total: # if the second payment is enough, it will give the user change and say bye
    print("Transaction approved! Your change is $%.2f" % change2)
    print("\nThanks for dining at Vivian's Cake Shop! See you again soon :)!")
elif payment2 < total: # if the payment still isn't enough, it will tell the user to come back later
    print("Sorry you still don’t have enough. Come back again later.")
    
