def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
number = 5
print(f"The factorial of {number} is: {factorial(number)}")
