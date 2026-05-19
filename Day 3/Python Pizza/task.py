print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0
#Check size of pizza and add corresponding price to bill
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Incorrect input. Please try again with either S, M or L")
#Add $3 to price if 'Y' is selected for pepperoni, otherwise do nothing
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
#Add $1 to price if 'Y' is selected extra cheese, otherwise do nothing
if extra_cheese == "Y":
    bill += 1
#Print out final price to user
print(f"Your final bill is: ${bill}.")