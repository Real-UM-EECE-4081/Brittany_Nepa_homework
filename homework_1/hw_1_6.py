#Write a Python function to calculate the factorial of a number (a non-negative integer). The function
#accepts the number as an argument.

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

x = int(input("Choose a number to find its factorial: "))
print(factorial(x))