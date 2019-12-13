'''
    Write a program that prints the numbers from 1 to 100. 
    But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
    For numbers which are multiples of both three and five print “FizzBuzz”.
'''

fizzbuzz_list = []
def print_numbers():
    for x in range(0,101):
        if x%3==0 and x%5==0:
            fizzbuzz_list.append(f"{x}: FizzBuzz")
        elif x%3==0:
            fizzbuzz_list.append(f"{x}: Fizz")
        elif x%5==0:
            fizzbuzz_list.append(f"{x}: Buzz")
        else:
            fizzbuzz_list.append(x)
    
    return(fizzbuzz_list)