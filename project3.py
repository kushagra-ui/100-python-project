print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

print("Welcome to treasure island \n Your Mission Is To Find Treasure")

print("There are two roads left & right choose one")
opt_1= input("enter your choice L for Left & R for Right : ")
if opt_1 == 'R':
    print("Game Over")
else:
    print("You have come to a lake")
    print("There is an island in the middle of the lake")
    print("You can wait for a boat or swim across")
    opt_2 = input("enter your choice W for wait & S for swim : ")
    if opt_2 == 'S':
        print ("Game Over")
    else:
        print("You have arrived at the island unharmed")
        print("There is a house with 3 doors")
        print("One red, one yellow and one blue")
        opt_3 = input("Which colour do you choose R for Red , Y for Yellow & B for Blue ? : ")
        if opt_3 == 'R':
            print("Game Over")
        elif opt_3 == 'Y':
            print("You Win")
        elif opt_3 == 'B':
            print("Game Over")
        else:
            print("Game Over")