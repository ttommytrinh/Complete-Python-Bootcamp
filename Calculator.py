'''
Simple calculator that does basic calculation from two user-inputted integers
'''

def calculator():
    if operation == "+":
        return(first_number+second_number)
    elif operation == "-":
        return(first_number-second_number)
    elif operation == "*":
        return(first_number*second_number)
    elif operation == "/":
        return(first_number/second_number)

#FIRST NUMBER INPUT    
while True:
    try:
        first_number = float(input("Enter a number: "))
        break
    except:
        print("Please enter a number")
        continue

#OPERATION        
while True:
    operation = input("Please enter an operation (+, -, *, /) : " )
    if operation == "+" or operation == "-" or operation == "*" or operation == "/":
        break
    else:
        continue

#SECOND NUMBER INPUT
while True:
    try:
        second_number = float(input("Enter a second number: "))
        break
    except:
        print("Please enter a number")
        continue
        
calculator()