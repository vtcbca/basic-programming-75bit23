def fibonacci(n, a=0, b=1):
    if n <= 0:
        return []
    else:
        return [a] + fibonacci(n-1, b, a+b)

terms = int(input("Enter a number for the number of terms: "))

if terms <= 0:
    print("Please enter a valid positive integer.")
else:
    fib_sequence = fibonacci(terms)
    print("The Fibonacci sequence of the numbers is:", fib_sequence)
