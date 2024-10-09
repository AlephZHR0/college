# 1. Dado um número inteiro, identificar se ele é par ou ímpar, emitir uma mensagem caso o número não seja inteiro.
def ex_01(num = 0):
    if num % 2 == 0:
        print("Este número é par")
    elif num % 2 == 1:
        print("Este número é impar")
    else:
        print("Este número não é inteiro")
# 2. Dado um número inteiro, calcular a soma dos dígitos desse número e verificar se essa soma é divisível por 3.
def ex_02(num = 0):
    summatory = 0
    while num != 0:
        summatory += num % 10
        # num //= 10
        num = (num / 10) - (num % 10 * 0.1)
    print(summatory)
    if summatory % 3 == 0:
        print("É divisível por 3")
    else:
        print("Não é divisível por 3")
# 3. Escreva um programa que receba um número inteiro e calcule o seu fatorial.
def ex_03(num = 0):
    factorial = 1
    for i in range(num, 1, -1):
        factorial *= i
    print(factorial)
# 4. Crie um programa que leia um número inteiro n e uma sequência de n números reais, e calcule a média aritmética desses números.
def ex_04(num = 0):
    summatory = num
    counter = 1
    user_input = None
    while user_input != "q":
        user_input = input("digite um número ou 'q' para sair: ").lower()
        if user_input == "q":
            break
        summatory += int(user_input)
        counter += 1
    mean = summatory / counter
    print(mean)
# 5. Escreva um programa que receba dois números inteiros e encontre o máximo divisor comum (MDC) entre eles.
def ex_05(x = 0, y = 0):
    if x < y: low = x
    else: low = y
    for num in range(1, low + 1):
        if x % num == 0 and y % num == 0:
            mdc = num
    print(mdc)
# 6. Dado um número inteiro positivo n, escreva um programa que verifique se ele é primo.
def ex_06(num = 1):
    divisors = 0
    for number in range(1, num + 1):
        if num % number == 0:
            divisors += 1
    if divisors == 2:
        print("É primo")
    else:
        print("Não é primo")
# 7. Escreva um programa que receba dois números inteiros e informe se o primeiro número é múltiplo do segundo número.
def ex_07(x, y):
    if x % y == 0:
        print("{} é multiplo de {}".format(y, x))
    else:
        print("{} não é multiplo de {}".format(y, x))
# 8. Dado um número inteiro, calcule a soma dos números primos menores ou iguais a ele.
def ex_08(num = 1):
    summatory = 0
    for number_1 in range(1, num + 1):
        count = 0
        for number_2 in range (1, number_1 + 1):
            if number_1 % number_2 == 0:
                count += 1
        if count == 2:
            summatory += number_1
    print(summatory)
# 9. Escreva um programa que receba uma sequência de números inteiros e calcule a média aritmética dos números pares.
def ex_09():
    summatory = 0
    counter = 0
    user_input = None
    while user_input != "q":
        user_input = input("Digite um número ou 'q' para sair: ").lower()
        if user_input == "q":
            break
        user_input = int(user_input)
        if user_input % 2 == 0:
            summatory += user_input
            counter += 1
    if counter != 0:
        mean = summatory / counter
        print(mean)
    else:
        print("Insisra ao menos um número valido")
# 10. Crie um programa que receba uma sequência de números inteiros e informe quantos deles são divisíveis por 3 e 5 ao mesmo tempo.
def ex_10():
    counter = 0
    user_input = None
    while user_input != "q":
        user_input = input("Digite um número ou 'q' para sair: ").lower()
        if user_input == "q":
            break
        user_input = int(user_input)
        if user_input % 3 == 0 and user_input % 5 == 0:
            counter += 1
    print(counter)
# 11. Dado um número inteiro, calcule a soma dos seus divisores próprios (ou seja, excluindo o próprio número).
def ex_11(num = 0):
    summatory = 0
    for number in range(1, num):
        if num % number == 0:
            summatory += number
    print(summatory)
# 12. Dado um número inteiro positivo, escreva um programa que verifique se ele é um número perfeito. Um número perfeito é um número inteiro positivo que é igual à soma de seus fatores, excluindo o próprio número.
def ex_12(num = 0):
    summatory = 0
    if num > 0:
        if num % 1 == 0:
            for number in range(1, num):
                if num % number == 0:
                    summatory += number
    if num == summatory:
        print("É um número perfeito")
    else:
        print("Não é um número perfeito")
## 13. Crie um programa que leia uma sequência de números inteiros e exiba o segundo maior número na sequência.
def ex_13():
    higher = 0
    sec_higher = 0
    user_input = None
    while user_input != "q":
        user_input = input("digite um número ou 'q' para sair: ").lower()
        if user_input == "q":
            break
        user_input = int(user_input)
        if user_input > higher:
            sec_higher = higher
            higher = user_input
    print(sec_higher)
# 14. Escreva um programa que receba um número inteiro positivo e determine quantos números primos existem entre 1 e esse número.
def ex_14(num = 0):
    prime_counter = 0
    for number_1 in range(1, num + 1):
        counter = 0
        for number_2 in range(1, number_1 + 1):
            if number_1 % number_2 == 0:
                counter += 1
        if counter == 2:
            prime_counter += 1
    print(prime_counter)
# 15. Escreva um programa que gere todos os números primos entre 1 e um número n escolhido pelo usuário.
def ex_15(num = 0):
    for number_01 in range(1, num + 1):
        count = 0
        for number_02 in range(1, number_01 + 1):
            if number_01 % number_02 == 0:
                count += 1
        if count == 2:
            print(number_01)
# 16. Escreva um programa que gere uma lista de todos os números primos de Mersenne menores que 1000. Um número primo de Mersenne é um número primo da forma2^p-1, onde p é um número primo.
def ex_16():
    for number_1 in range(1, 15):
        counter = 0
        for number_2 in range(1, number_1 + 1):
            if number_1 % number_2 == 0:
                counter += 1
        if counter == 2:
            p = number_1
            num_merc = 2 ** p - 1
            if num_merc < 1000:
                print(num_merc)
            else:
                break
# 17. Crie um programa que leia um número inteiro e verifique se o número é um palíndromo.
def ex_17(num = 0):
    digits = 0
    num_counter = num 
    while num_counter != 0:
        num_counter //= 10
        digits += 1
    l_to_r_counter = digits
    for i in range(0, digits):
        right_number = (num // 10 ** i) % (10) # 7
        left_number = (num // 10 ** (l_to_r_counter - 1)) % 10 # 8
        if left_number != right_number:
            print("Não é um palíndromo")
            break
        elif i == digits - 1:
            print("É um palíndromo")
        l_to_r_counter -= 1
