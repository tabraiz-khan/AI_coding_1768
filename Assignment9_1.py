'''
This module contains functions to find the maximum and minimum numbers in a list, as well as a simple calculator function that performs basic arithmetic operations.
The find_max function takes a list of numbers as input and returns the maximum number in the list. The find_min function does the same for the minimum number. The calculator function takes two numbers and an operation as input and returns the result of the specified operation.
The module also includes test cases for the is_valid_username function, which checks if a given username is valid based on specific criteria.
Author: Tabraiz Khan
`'''
# generate docstring for documentation of the function find_max(numbers)
# def find_max(numbers):
#     '''
#     This function takes a list of numbers as input and returns the maximum number in the list.
    
#     :param numbers: A list of numbers
#     :return: The maximum number in the list
    
#     >>> find_max([1, 2, 3, 4, 5])
#     5
#     >>> find_max([-1, -2, -3, -4, -5])
#     -1
#     >>> find_max([0, 0, 0])
#     0
#     >>> find_max([1.5, 2.5, 3.5])
#     3.5
#     >>> find_max([1])
#     1
#     '''
#     if not numbers:
#         return None
#     max_num = numbers[0]
#     for num in numbers:
#         if num > max_num:
#             max_num = num
#     return max_num

# do the same with inline documentation and block documentation for the min function. don't use docstring.

def find_min(numbers):
    # This function takes a list of numbers as input and returns the minimum number in the list.
    # It checks if the list is empty and returns None if it is. Otherwise, it initializes the minimum number to the first element of the list and iterates through the list to find the minimum number.
    if not numbers:
        return None
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

# print(find_max.__doc__)


# write a function along with documentation of a calculator with functions add, subtract, multiply and divide.
def calculator(a, b, operation):
    '''
    This function performs basic arithmetic operations (addition, subtraction, multiplication, and division) on two numbers based on the specified operation.
    
    :param a: The first number
    :param b: The second number
    :param operation: A string specifying the operation ('add', 'subtract', 'multiply', 'divide')
    :return: The result of the specified operation on the two numbers

    '''
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            return 'Error: Division by zero'
        return a / b
    else:
        return 'Error: Invalid operation'

# command is python -m pydoc -w assignment9_1.py to generate html documentation for the file. This will create a file named assignment9_1.html in the current directory. You can open this file in a web browser to view the documentation.
# another command is python -m pydoc -p 8080 or something to view in server