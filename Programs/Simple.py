

def is_simple(a):
    i = 2
    if a != 1:
        while i*i <= a:
            if a%i == 0:
                return False
            i += 1
        return True
    else:
        return False
print(is_simple(3))