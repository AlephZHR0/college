def ex_1(number):
    summatory = 0
    for decimal_place in str(number):
        summatory += int(decimal_place)
    print(summatory)
    if summatory % 3 == 0:
        print("A soma dos dígitos é divisível por 3")
    else:
        print("A soma dos dígitos não é divisível por 3") 

def ex_2(number):
    fat = 1
    for i in range(1, number + 1):
        fat *= i
    print(fat)