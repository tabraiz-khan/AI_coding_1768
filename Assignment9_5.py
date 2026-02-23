'''
generate code and documentation for a math utility module with functions square, cube and factorial. The square function takes a number as input and returns its square. The cube function does the same for the cube of the number. The factorial function calculates the factorial of a given number using recursion. The module also includes test cases for the is_valid_username function, which checks if a given username is valid based on specific criteria.
Author: Tabraiz Khan

'''
def square(num):
    '''
    This function takes a number as input and returns its square.
    
    :param num: A number
    :return: The square of the number
    
    '''
    return num ** 2

def cube(num):
    '''
    This function takes a number as input and returns its cube.
    
    :param num: A number
    :return: The cube of the number

    '''
    return num ** 3
def factorial(n):
    '''

    This function calculates the factorial of a given number using recursion.
    :param n: A non-negative integer
    :return: The factorial of the number

    '''
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(square.__doc__)
#code for running on a browser is python -m pydoc -p 8080
#code for html is python -m pydoc -w 8080
#code for documentation is python -m pydoc Assignment9_5.py
