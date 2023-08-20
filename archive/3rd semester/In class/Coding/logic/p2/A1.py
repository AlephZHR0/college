# an = a1 + (n - 1) * d
def ex_1(numero_de_termos,primeiro_termo, razão):
    def ultimo_termo(numero_de_termos, razão):
        return primeiro_termo + (numero_de_termos - 1) * razão
    
    return (numero_de_termos / 2) * (primeiro_termo + ultimo_termo(numero_de_termos, razão))

def ex_2a(numero_de_termos, primeiro_termo, base):
    sum = 0
    for i in range(1, numero_de_termos + 1):
        sum += primeiro_termo + (base ** i)
    return sum

def ex_2b(numero_de_termos, primeiro_termo, base):
    sum = 0
    for i in range(1, numero_de_termos + 1):
        sum += primeiro_termo * (base ** i)
    return sum

def ex_3(numero_de_termos):
    sum = 0
    for i in range(1, numero_de_termos + 1):
        sum += (-1)**i * (1 / i)
    return sum

def ex_4(n):
    sum = 0
    for i in range(n + 1):
        sum += (-1)**i / i**2
    return sum

def ex_05(n):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    sum = 0
    for i in range(n + 1):
        (-1)**i * i / factorial(i)
    return sum

def ex_06a(n):
    sum = 0
    for i in range(1, n + 1):
        sum += (-1/2)**i
    return sum

def ex_06b(n):
    def fact(n):
        if n == 0:
            return 1
        else:
            return n * fact(n - 1)

    sum = 0
    for i in range(n):
        (1 + i) / fact(1 + 2 * i)
        return sum