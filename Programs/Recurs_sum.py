def summa(n):
    if n<2:
        return  n==1
    else:
        s = n+summa(n-1)
        return s



print(summa(6))