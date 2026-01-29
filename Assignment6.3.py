# Generate a function that displays all Automorphic numbers from 1 to 1000 using a for loop all in one function.
def display_automorphic_numbers():
    automorphic_numbers = []
    for num in range(1, 1001):
        square = num ** 2
        if str(square).endswith(str(num)):
            automorphic_numbers.append(num)
    print("Automorphic numbers from 1 to 1000 are:", automorphic_numbers)
# Call the function to display the automorphic numbers
# display_automorphic_numbers()

# Generate a function that displays all Automorphic numbers from 1 to 1000 using a while loop all in one function.
def display_automorphic_numbers_while():
    automorphic_numbers = []
    num = 1
    while num <= 1000:
        square = num ** 2
        if str(square).endswith(str(num)):
            automorphic_numbers.append(num)
        num += 1
    print("Automorphic numbers from 1 to 1000 are:", automorphic_numbers)
#calculate the time to run both the functions 
# import time
# start_for = time.time()
# display_automorphic_numbers()
# end_for = time.time()
# start_while = time.time()
# display_automorphic_numbers_while()
# end_while = time.time()
# print(f"Time taken by for loop: {end_for - start_for} seconds")
# print(f"Time taken by while loop: {end_while - start_while} seconds")


# Generate a function to classify online shopping feedback as postivie,neutral, or negative based on  numerical rating of 1 to 5.
def classify_feedback(rating):
    if rating >= 4:
        return "Positive"
    elif rating == 3:
        return "Neutral"
    elif rating >= 1:
        return "Negative"
    else:
        return "Invalid rating"
# do the same using dictionary mapping
def classify_feedback_dict(rating): 
    feedback_map = {
        5: "Positive",
        4: "Positive",
        3: "Neutral",
        2: "Negative",
        1: "Negative"
    }
    return feedback_map.get(rating, "Invalid rating")
# Test the functions
# print(classify_feedback_dict("B"))  # Positive 

class Teacher:
    def __init__(self,teacher_id,teacher_name,subject,experience):
        self.teacher_id=teacher_id
        self.teacher_name=teacher_name
        self.subject=subject
        self.experience=experience
    def display_details(self):
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Teacher Name: {self.teacher_name}")
        print(f"Subject: {self.subject}")
        print(f"Experience: {self.experience} years")

# Create an instance of the Teacher class and display details
# teacher1 = Teacher(101, "Alice Smith", "Mathematics", 10)
# teacher1.display_details()

#generate a function that takes a phone number as input and validates if it is an indian phone number or not.
import re
def validate_indian_phone_number(phone_number):
    pattern = re.compile(r'^[6-9]\d{9}$')
    if pattern.match(phone_number):
        return True
    else:
        return False
# Test the function
# print(validate_indian_phone_number("7876543210"))  # True

# Armstrong_Numbers(1,1000)
def Armstrong_Numbers(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        order = len(str(num))
        sum_of_powers = sum(int(digit) ** order for digit in str(num))
        if num == sum_of_powers:
            armstrong_numbers.append(num)
    print(f"Armstrong numbers from {start} to {end} are:", armstrong_numbers)
# Test the function
# Armstrong_Numbers(1, 1000)

# HappyNumbers(1,500)-> 1,7,etc
def HappyNumbers(start, end):
    happy_numbers = []

    def is_happy(n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1

    for num in range(start, end + 1):
        if is_happy(num):
            happy_numbers.append(num)

    print(f"Happy numbers from {start} to {end} are:", happy_numbers)   
# Test the function
# HappyNumbers(1, 500)

""" student = {
    "personal": {
        "name": {
            "first": "Ayaan",
            "last": "Khan"
        }
    },
    "academic": {
        "branch": "CSE",
        "performance": {
            "sgpa": 8.7
        }
    }
}

output->("Arjun Mehta", "ME", 7.9) 
student = {
    "personal": {
        "name": {
            "first": "Ayaan",
            "last": "Khan"
        }
    },
    "academic": {
        "branch": "CSE",
        "performance": {
            "sgpa": 8.7
        }
    }
}
("Ayaan Khan", "CSE", 8.7)



"""


def extract_student_info(student):
    first_name = student["personal"]["name"]["first"]
    last_name = student["personal"]["name"]["last"]
    branch = student["academic"]["branch"]
    sgpa = student["academic"]["performance"]["sgpa"]
    full_name = f"{first_name} {last_name}"
    return full_name, branch, sgpa
# Test the function
print(extract_student_info({
    "personal": {
        "name": {
            "first": "Arjun",
            "last": "Mehta"
        }
    },
    "academic": {
        "branch": "ME",
        "performance": {
            "sgpa": 7.9
        }
    }
}))  # ("Arjun Mehta", "ME", 7.9)

# prefect_numbers(1,1000):-> 6,28,496
def perfect_numbers(start, end):    
    perfect_nums = []
    for num in range(start, end + 1):
        divisors_sum = sum(i for i in range(1, num) if num % i == 0)
        if divisors_sum == num:
            perfect_nums.append(num)
    print(f"Perfect numbers from {start} to {end} are:", perfect_nums)

# Test the function
# perfect_numbers(1, 1000)
perfect_numbers(1, 1000)







