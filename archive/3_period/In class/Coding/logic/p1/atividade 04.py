# 1. Escreva um programa que leia uma sequência de números inteiros e identifique subsequências crescentes de maior comprimento.
def ex_01():
    usr_input = int(input("Digite um número ou 'q' para receber o resultado: "))
    text = ""
    highest_number = (usr_input)
    text += "{} ".format(usr_input)
    while usr_input != "q":
        if int(usr_input) > highest_number:
            text += "{} ".format(int(usr_input))
            highest_number = int(usr_input)
        usr_input = input("Digite um número ou 'q' para receber o resultado: ")
    return print(text)
# 2. Dado um número inteiro n, escreva um programa que gere os n primeiros números da sequência de Fibonacci.
def ex_02(n):
    a = 0
    b = 1
    for _ in range(n):
        print(b)
        fibonacci = a + b
        a = b
        b = fibonacci
# 3. Escreva um programa que leia uma lista de números inteiros e identifique o maior produto que pode ser obtido multiplicando dois elementos da lista.
def ex_03():
    hpv = 0
    shpv = 0
    lnv = 0
    slnv = 0
    usr_input = None
    while usr_input != "q":
        usr_input = input("Digite um número ou 'q' para receber o resultado: ")
        if usr_input == "q":
            break
        else:
            usr_input = int(usr_input)
            if usr_input > shpv:
                if usr_input > hpv:
                    shpv = hpv
                    hpv = usr_input
                else:
                    shpv = usr_input
            if usr_input < slnv:
                if usr_input < lnv:
                    slnv = lnv
                    lnv = usr_input
                else:
                    slnv = usr_input
    if hpv * shpv > lnv * slnv:
        hn = hpv * shpv
    else:
        hn = lnv * slnv
    return print("O maior produto será: {}".format(hn))
# 4. Dado um número inteiro positivo n, escreva um programa que gere todos os números perfeitos até n. Exiba a sequência.
def ex_04(n):
    def perfect_number_check(number_to_check):
        summatory = 0
        for number in range(1, int(number_to_check/2) + 1):
            if number_to_check % number == 0:
                summatory += number
        if summatory == number_to_check:
            return True
        else:
            return False

    for number in range(1, n + 1):
        if perfect_number_check(number):
            print(number)
# 5. Crie um programa que leia uma sequência de números inteiros e encontre a subsequência contínua de maior soma.
IS_ON = True
TEMP = None
def ex_05():
    def get_sequency():
        global TEMP
        def is_in_sequence(predecessor, new_number):
            if predecessor == new_number - 1 or predecessor == new_number + 1:
                return True
            else:
                return False
        
        def get_a_number():
            global IS_ON
            user_input = input("Digite um número ou 'q' para receber o resultado: ")
            if user_input !="q":
                return int(user_input)
            else:
                IS_ON = False
                return False
            
        if TEMP != None:
            predecessor = TEMP
            TEMP = None
        else:
            predecessor = get_a_number()
        sequence = "{}".format(predecessor)
        sequence_summatory = predecessor
        new_number = get_a_number()
        while is_in_sequence(predecessor, new_number):
            sequence += ", {}".format(new_number)
            sequence_summatory += new_number
            predecessor = new_number
            new_number = get_a_number()
            TEMP = new_number
        return sequence, sequence_summatory
        
    def compare_sequences(sequence_1, sequence_2):
        if sequence_1[1] > sequence_2[1]:
            return sequence_1
        else:
            return sequence_2

    higher_sequency = get_sequency()
    while IS_ON:
        sequency_2 = get_sequency()
        higher_sequency = compare_sequences(higher_sequency, sequency_2)
    print(higher_sequency[0])
# 6. Escreva um programa que leia uma sequência de números inteiros e determine se a sequência pode ser ordenada em ordem crescente com no máximo uma troca de elementos.
def ex_06():
    def get_a_number():
        user_input = input("Digite um número ou qualquer outra coisa para receber o resultado: ")
        if (user_input).isnumeric() == True:
            return int(user_input)
        else:
            return False
    
    def growing(predecessor, new_number):
        if predecessor < new_number:
            return True
        else:
            return False

    number_of_changes_to_be_growing = 0
    predecessor = get_a_number()
    new_number = get_a_number()
    while True:
        if not growing(predecessor, new_number):
            number_of_changes_to_be_growing += 1
        new_number = get_a_number()
        if new_number == False:
            break
    if number_of_changes_to_be_growing > 1:
        print("Não é possível ordenar em ordem crescente com no máximo uma troca de elementos.")
    else:
        print("É possível ordenar em ordem crescente com no máximo uma troca de elementos.")
# 7. Escreva um programa que calcule a soma dos n primeiros termos da série geométrica com razão r e primeiro termo a, onde n, r e a são fornecidos pelo usuário.
def ex_07(n_termos, razão, a):
    summatory = 0
    for i in range(0, razão + 1):
        summatory += a * razão ** i
    print(summatory)
# 8. Escreva um programa que leia uma sequência de números inteiros e determine se a sequência é uma progressão aritmética, uma progressão geométrica ou nenhuma das duas.
def ex_08():
    def get_a_number():
        user_input = input("Digite um número ou qualquer outra coisa para receber o resultado: ")
        if (user_input).isnumeric() == True:
            return int(user_input)
        else:
            return False
        
    def is_geom(p_number, n_number, reason):
        if p_number * reason == n_number:
            return True
        else:
            return False
    
    def is_arit(p_number, n_number, reason):
        if p_number + reason == n_number:
            return True
        else:
            return False
        
    IS_ON = True
    IS_ARIT = True
    IS_GEOM = True
    first_term = get_a_number()
    second_term = get_a_number()
    reason_pa = second_term - first_term
    reason_pg = second_term / first_term
    while IS_ON:
        new_number = get_a_number()
        if not is_arit(second_term, new_number, reason_pa):
            IS_ARIT = False
        if not is_geom(second_term, new_number, reason_pg):
            IS_GEOM = False
        second_term = new_number
    if IS_ARIT == True:
        print("É uma progressão aritmética.")
    elif IS_GEOM == True:
        print("É uma progressão geométrica.")
    else:
        print("Não é uma progressão aritmética nem geométrica.")
# 9. Dado um número inteiro positivo n, escreva um programa que calcule a soma dos quadrados dos n primeiros números naturais.
def ex_09a(n):
    start_time = time.time()
    for i in range(1, n + 1):
        summatory += i ** 2
    print(summatory)
# 09. Dado um número inteiro positivo n, escreva um programa que calcule a soma dos quadrados dos n primeiros números naturais.
def ex_09b(n):
    print((n * (n + 1) * (2 * n + 1)) / 6)
# 10. Escreva um programa que dado um número par maior que 2, exiba sua decomposição de Goldbach (ou seja, escreva-o como soma de 2 números primos). Tente encontrar algum número inteiro par maior que 2 que não possua decomposição de Goldbach.
def ex_10(n):
    def is_prime(n):
        for i in range(2, int(n / 2)):
            if n % i == 0:
                return False
        return True
    for i in range(2, n + 1):
        if is_prime(i) and is_prime(n - i):
            print("{} = {} + {}".format(n, i, n - i))
            break
# 11. Considere o polinômio de Euler dado por P(n)=n^2+n+41. É verdade dizer que os resultados de P(1), P(2), P(3),... são todos números primos? Faça a verificação
def ex_11():
    def is_prime(number):
        for i in range(2, int(number / 2)):
            if number % i == 0:
                print("Divisor: {}".format(i))
                return False
        return True
    
    def pn_euler(num):
        return num ** 2 + num + 41

    for i in range(1, 100):
        if not is_prime(pn_euler(i)):
            print("Não é verdade, pois {} ao ser passado pela função, torna-se {} que não é primo.".format(i, pn_euler(i)))
            break