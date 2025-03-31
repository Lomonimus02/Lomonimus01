def multipliers(num):
    list_simple = []
    simple = 2
    while num > 1:
        if num % simple == 0:
            list_simple.append(simple)
            num = num/simple
        else:
            simple += 1
    return list_simple
print(multipliers(20))
'''эта программа раскладывает число на простые множители и выводит их списком'''