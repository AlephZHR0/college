def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def exp(n):
    for i in range(n + 1):
        pass

def sin(n):
    sum = 0
    for i in range(n + 1):
        sum += (-1)**i / factorial(2*i + 1)
    return sum

def cos(n):
    sum = 0
    for i in range(n):
        sum += (-1)**i / factorial(2*i)
    return sum