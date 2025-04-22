# creating a password generator
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')','-','=','+']
ip_letters=int(input("How many letters would you like in your password\n"))
ip_symbols=int(input("How many symbol would you like in your password\n"))
ip_numbers=int(input("How many number would you like in your password\n"))
ip_difficulty=input("enter the difficulty level")


 
 
 # Easy password
if ip_difficulty == "Easy" or '1':
    easy_password=""

    for char in range (1,ip_letters + 1):
         
         password_letters= random.choice(letters)
         a= password_letters
         easy_password += str(a)
    for num in range (1,ip_numbers + 1):
         password_numbers= random.choice(numbers)
         b= password_numbers
         easy_password += str(b)
    for sym in range (1,ip_symbols + 1):
         password_symbols= random.choice(symbols)
         c= password_symbols
         easy_password += str(c)
    print(easy_password)
 
 # Hard password
hard_password = ""
if ip_difficulty == "Hard" or '2':
     hard_password == ''.join(random.sample(easy_password, len(easy_password)))
     print(hard_password)