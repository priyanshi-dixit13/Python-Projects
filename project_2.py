print("WELCOME TO PYTHON PIZZA HUT🍕")

# -------------------------pizza size---------------------------------

size= input("what size of pizza do you want? Small(S), Medium(M), Large(L): ")

if size == "S" or size =="s":
   bill = 150
elif size == "M" or "m":
   bill = 200
elif size == "L" or "l":
    bill = 250
else:
    print("Invalid pizza size!")
    bill = 0    

#----------------------------toppings---------------------------------
cheese = input("Do you want extra cheese? Y or N: ")
if cheese == "Y" or cheese == "y":
    bill += 30
onion = input("Do you want extra onion? Y or N: ")
if onion == "Y" or onion == "y":
    bill += 20
tomato = input("Do you want extra tomato? Y or N: ")
if tomato == "Y" or tomato == "y":      
    bill += 30
capsicum = input("Do you want extra capsicum? Y or N: ")
if capsicum == "Y" or capsicum == "y":
    bill += 30
corn = input("Do you want extra corn? Y or N: ")
if corn == "Y" or corn == "y":
    bill += 20

#----------------------------------final bill---------------------------
print("--------------------------------------") 
print("YOUR FINAL BILL IS: RS.", bill)



