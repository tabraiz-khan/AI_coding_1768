# import unittest


# def check_even(n):
#     '''
#     Docstring for check_even
    
#     :param n: Description
#     >>> check_even(4)
#     True
#     >>> check_even(5)
#     False
#     '''
#     if n%2==0:
#         return True
#     else:
#         return False
    
# assert check_even(4) == True
# assert check_even(5) == False

# # write a python function add(a,b) to add two numbers. Use the unittest to test whether the function is working correctly or not.
# def add(a,b):
#     return a+b
# class TestAddFunction(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(2,3),5)
#         self.assertEqual(add(-1,1),0)
#         self.assertEqual(add(0,0),0)

#     def test_boundary(self):
#         self.assertEqual(add(1e10,1e10),2e10)
#         self.assertEqual(add(-1e10,-1e10),-2e10)

#     def test_edge_cases(self):
#         self.assertEqual(add(0,5),5)
#         self.assertEqual(add(5,0),5)
#         self.assertEqual(add(-5,-5),-10)
# if __name__ == '__main__':
#     unittest.main()

# import pytest
# def sub(a,b):
#     return a-b

# def test_sub():
#     assert sub(5,3)==2
#     assert sub(-1,1)==-2
#     assert sub(0,0)==0     
# 
# write a python function that checks is_valid_username(username) , namelength 5 to 15,only alphabets and digits, shouldn't start with digit , no spaces allowed and generate 5 testcases of assert
def is_valid_username(username):
   if len(username)<5 or len(username)>15:
        return False
   if not username[0].isalpha():
        return False
   for char in username:
        if not (char.isalpha() or char.isdigit()):
            return False
        
   return True
# Test cases
assert is_valid_username("user123") == True
assert is_valid_username("123user") == False
assert is_valid_username("user name") == False
assert is_valid_username("us") == False
assert is_valid_username("thisisaverylongusername") == False


# check if a number is abudndant or not. An abundant number is a number for which the sum of its proper divisors is greater than the number itself. For example, 12 is an abundant number because its proper divisors are 1, 2, 3, 4, and 6, and their sum is 16, which is greater than 12. and generate testcases with unittest library

def is_abundant(n):
    if n < 12:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum > n
# Test cases
import unittest
class TestAbundantNumber(unittest.TestCase):
    def test_abundant(self):
        self.assertTrue(is_abundant(12))
        self.assertTrue(is_abundant(18))
        self.assertFalse(is_abundant(10))
        self.assertFalse(is_abundant(11))
        self.assertFalse(is_abundant(1))
if __name__ == '__main__':
    unittest.main()


# write a function to get sum of the numbers digits and test it using pytest library
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))
# Test cases
import pytest
def test_sum_of_digits():
    assert sum_of_digits(123) == 6
    assert sum_of_digits(-456) == 15
    assert sum_of_digits(0) == 0
    assert sum_of_digits(999) == 27
    assert sum_of_digits(-10) == 1








