def ex_1(number = 0):
    if type(number) == int:
        if number % 2 == 0:
            print("even")
        if number % 2 != 0:
            print("odd")
    else:
        print("The number isn't an integer")

def ex_2(a = 1, b = 0, c = 0):
    # positive root:
    positive_resut = (- b + ((b ** 2 - 4 * a * c) ** (1 / 2))) / (2 * a)
    # negative root:
    negative_result = (- b - ((b ** 2 - 4 * a * c) ** (1 / 2))) / (2 * a)
    print("Positive: {}\nNegative: {}".format(positive_resut, negative_result))
    return [positive_resut, negative_result]

def ex_3(salary = 0, bool = False):
    if salary < 2000:
        new_salary = salary * 1.08
    elif salary > 4000:
        new_salary = salary * 1.03
    else:
        new_salary = salary * 1.05
    if bool:
        new_salary += 1000
    print("The new salary is : {}".format(new_salary))
    return salary

def ex_4(x = 0, rep = 1):
    ini_pow = 25
    ini_div = 1
    signal = 0
    summatory = 0
    for i in range(rep):
        print(i)
        if signal % 2 == 0:
            summatory += ((x) ** ini_pow) / ini_div
        else:
            summatory -= ((x) ** ini_pow) / ini_div
        ini_pow -= 1
        ini_div += 1
        signal += 1
    print(summatory)
    return summatory

def ex_5(x, n):
    from math import factorial
    summatory = 0
    for i in range (1, 1000):
        summatory += ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
    print("sin({}) using a Taylor series with {} decimal places of precision is: {:.{}f}".format(x, n, summatory, n))