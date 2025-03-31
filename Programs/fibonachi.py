def fibonacciI(n):
    if 0 < n < 3:
        return 1
    return fibonacciI(n - 1) + fibonacciI(n - 2)


print(fibonacciI(3))