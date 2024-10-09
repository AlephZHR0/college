def soma(n):
    summatory = 0
    if n == 0:
        return 0
    else:
        return n + soma(n-1)
print(soma(3))
soma(input("soma: "))