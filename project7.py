# Hangman Game 
import random
print("Welcome the Hangman Game ")
hangman = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========''']


word_list=["ant " ,"baboon", "badger" , "bat", "bear", "beaver" ,"camel" , "cat " , "clam", "cobra"," cougar"
         "coyote"," crow ", "deer", "dog" , "donkey ","duck ","eagle ","ferret" ,"fox ", "frog", "goat "]
       
lives = 6
print("The number of lives that is allot to you is : ", lives)

choosen_word = random.choice(word_list)
# print(choosen_word)

placeholder = "" 
word_length = len(choosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)    
game_over = False
correct_letters = []

while not game_over:
    
  guess = input("guess a letter : ").lower()
  print(guess)
  display = ""

  for letter in choosen_word:
     if letter == guess:
        display += letter
        correct_letters.append(guess)
     elif letter in correct_letters:
        display+= letter
     
     else :
        display += "_"

  print(display)   
  if guess not in choosen_word:
    lives-= 1
    print (f"you have {lives} left ")
    if lives == 0 :
     print("You have 0 lives left, Game Over 🥲")
     game_over = True
  elif "_" not in display :
    game_over = True
    print("You win 😁")   
 






       


