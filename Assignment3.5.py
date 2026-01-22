# give me a python code checks if an year is leap year or not
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
# Example usage
year = 1600
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

#gcd(12,18)=6
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(gcd(12, 48))  # Output: 6

'''lcm(4,6)=12
lcm(5,10)=10
lcm(7,3)=21
lcm(0,6)=?'''
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
print(lcm(4, 10))  # Output: 12

# convert a number from binary to decimal for only valid inputs, if invalid inputs handle them appropriately
def binary_to_decimal(binary_str):
    try:
        decimal_value = int(binary_str, 2)
        return decimal_value
    except ValueError:
        return "Invalid binary number"
# Example usage
binary_input = "1011"

print(binary_to_decimal("abcd"))  # Output: 11

# we are given a number n,find decimal(n)
#decimal(1011)=11
def decimal(n):
    decimal_value = 0
    power = 0
    while n > 0:
        digit = n % 10
        decimal_value += digit * (2 ** power)
        n //= 10
        power += 1
    return decimal_value
print(decimal(1011))  # Output: 11

# harshadnumber,18
# not harshadnumber,19
def is_harshad_number(n):
    digit_sum = sum(int(digit) for digit in str(n))
    return n % digit_sum == 0   
# Example usage
number = 18