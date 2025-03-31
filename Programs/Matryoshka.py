def matryoshka(n):
    if n == 1:
        print("Матрешечка")
    else:
        print("Верх матрешки = ", n)
        matryoshka(n-1)
        print("Низ матрешки = ", n)


print(matryoshka(6))