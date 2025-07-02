def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4))

factorial_cache = {}

def factorial2(n):
    if n in factorial_cache:
        return factorial_cache[n]

    if n == 0 or n == 1:
        result = 1
    else:
        result = n * factorial(n - 1)

    factorial_cache[n] = result
    return result
