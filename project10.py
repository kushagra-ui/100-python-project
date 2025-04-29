print("Welcome to the calculator! ")
print('''___________________
| _________________ |
| | JO 0. | | 
| |_________________| |
| ___ ___ ___ ___ |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|''')

def add(n1 , n2 ):
    return n1+n2
def subtract( n1 , n2):
    return n1-n2
def divide(n1,n2):
    return n1/n2
def multiply(n1,n2):
    return n1*n2
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/":divide
}
# print(operations["*"](4,8))
def calculator():
   should_accumulate = True
   while should_accumulate:
    num1 = float(input("What is the first number ? \n"))
    for symbol in operations :
      print(symbol)
    operation_symbol = input("What is an operation")
    num2 =  float(input("What is the second number \n "))
    answer = operations[operation_symbol](num1,num2)
    print(f"{num1} {operation_symbol} {num2} = {answer} " )
    choice = input(f" Type 'y' to continue calculation with {answer} or type 'n' to start a new calculation ")
    if choice == 'y':
       print(f"Your previous num is {answer}")
       for symbol in operations :
        print(symbol)
       operation_symbol = input("What is an operation")
       num2 =  float(input("What is the second number \n "))
       answer = operations[operation_symbol](answer,num2)

    
     

    else :
      should_accumulate = False
      print("\n*20")
      calculator()

calculator()


