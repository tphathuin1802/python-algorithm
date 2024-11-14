def fibonacci(n):
    if n < 0:
        return -1
    elif (n == 0):
        return n == 0
    elif (n == 1 or n == 2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

try:
    n = int(input("enter the number of numbers: "))
    if n < 0:
        raise ValueError
    print("Must integer value and more or equal to zero")
except ValueError:
    print("Must enter appropriate value")

