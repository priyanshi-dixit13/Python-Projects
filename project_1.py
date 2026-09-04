print("Welcome to the roller coaster game🎮")

height= int(input("Enter your height in cm:"))
age= int(input("Enter your age in years:"))

if  height < 100:
    print("Not Eligible")
elif age <= 12:
    print("Can Ride")    
    print("Ticket price will be: RS.50")
elif  age <= 18:
    print("Can Ride")    
    print("Ticket price will be: RS.70")
elif age <= 60:
    print("Can Ride")    
    print("Ticket price will be: RS.100")
else:
    print("Not Eligible")
    