
# write a python function to print if a given number is palindrome or not
def is_palindrome(num):
    original_num=str(num)
    reversed_num=original_num[::-1]
    if(original_num==reversed_num):
        return True
    else:
        return False
    

# fact(4)=24
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

# armstrong(153)=Armstrong
# armstrong(123)=Not Armstrong
# armstrong(370)=Armstrong
def is_armstrong(num):
    str_num=str(num)
    num_digits=len(str_num)
    sum_of_powers=0
    for digit in str_num:
        sum_of_powers+=int(digit)**num_digits
    if(sum_of_powers==num):
        return True
    else:
        return False

'''
check if a number is perfect number or not ,return true false'''
def is_perfect_number(num):
    if num <= 1:
        return False
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num
# print(is_perfect_number(6))  # True
# print(is_perfect_number(28)) # True   

'''classify(5) odd
classify(10) even
classify(a) invalid input'''
def classify_number(n):
    if not isinstance(n, int):
        return "invalid input"
    if n % 2 == 0:
        return "even"
    else:
        return "odd"
print(classify_number("abc"))