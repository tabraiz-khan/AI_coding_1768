#Q1 . give code for factorial without function

# num=5
# factorial=1
# for i in range(1,num+1):
#     factorial=factorial*i
# print("Factorial of",num,"is",factorial)  
# 
#Q2 . Optimize q1
num=5
factorial=1  
while num>1:
    factorial=factorial*num
    num-=1  
print("Factorial is",factorial)
#Q3. Factorial using function
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print("Factorial using function is",factorial(5))

#Q4. compare the above codes for usecases and give comment

# The first code snippet calculates the factorial of a number using an iterative approach with a for loop. It is straightforward and easy to understand for small numbers. However, it may not be as efficient for very large numbers due to the overhead of loop control.

#Q5. give same thign using loop and recursion 2 different codes
# Iterative approach using loop
def factorial_iterative(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result   
print("Factorial using iterative approach:",factorial_iterative(5))
# Recursive approach
def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial_recursive(n-1)
print("Factorial using recursive approach:",factorial_recursive(5)) 
# The iterative approach is generally more efficient in terms of memory usage since it doesn't involve the overhead of multiple function calls. The recursive approach, while elegant and easier to read for some, can lead to stack overflow errors for large inputs due to deep recursion.