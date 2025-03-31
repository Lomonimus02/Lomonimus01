from Programs.Simple import is_simple


def R_n_s_n(num):
    num += 1
    while 1:
        if is_simple(num):
            return num
        num += 1


def L_n_s_n(num):
    num -= 1
    while 1:
        if is_simple(num):
            return num
        num -= 1


def n_s_n(num):
    x = R_n_s_n(num)
    y = L_n_s_n(num)
    if x - num <= num - y:
        return x
    else:
        return y


num = 0
print(n_s_n(num))
print(is_simple(1))