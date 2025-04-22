# stone paper scissor game
import random
print("Welcome to the Rock Paper Scissor Game")

R = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
P = '''   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
S = '''   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Enter your choice Stone, Write 0 for Rock, 1 for Paper, 2 for scissor")
user_choice = int(input("Make ur choice: "))
if user_choice == 0:
    print(R)
    print("Rock")
elif user_choice ==1:
    print(P)  
    print("Paper") 
elif user_choice ==2:
    print(S)
    print("scissor")
else:
    print("Invalid choice")
computer_choice = random.randint(0,2)
if computer_choice ==  0:
    print(R)
    print("Rock")
elif computer_choice ==1:
    print(P)
    print("Paper")
elif computer_choice== 2:
    print(S)
    print("scissor")
if computer_choice == user_choice:
     print("It's a tie")
elif computer_choice == 0 and user_choice == 1:
     print("You win")
elif computer_choice==1 and user_choice == 2:
     print("You win")
elif computer_choice==2 and user_choice == 0:
     print("You win")
else:
     print("You lose")              
            