print("Welcome to the Python pizza delivery")
size = input("what size pizza do u want ? S,M or L:")
peperoni = input("do u want peperoni? y or n :")
cheese = input("do u want extra cheese or not ? Y or N :")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size =="L":
    bill += 25
else:
    print("you give wrong input:")
if peperoni == "Y":
    if size == "s":
        bill += 2
    else :
        bill += 3 
if cheese == "Y":
    bill += 1
print(f"Your final bill is :{bill}")                    
     

