'''
Reverses a user-inputted string
'''

input_string = (input("What string would you like to have reversed?"))

string_list = [x for x in input_string]

def reverse_string():
    new_string_list = string_list[::-1]
    new_string = "".join(new_string_list)
    return(new_string)

reverse_string()
