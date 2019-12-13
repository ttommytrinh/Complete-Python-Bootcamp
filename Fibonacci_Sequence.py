def fibonacci(number):
    a,b = 1, 1
    fibonacci_list = []
    for x in range(number): 
        fibonacci_list.append(a)
        a, b = b, a+b
    return(fibonacci_list)