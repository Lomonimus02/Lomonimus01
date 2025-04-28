def mmatrix(matrix_1, matrix_2):
    strk_1 = len(matrix_1)
    stlb_1 = len(matrix_1[0])

    strk_2 = len(matrix_2)
    stlb_2 = len(matrix_2[0])

    if stlb_1 != strk_2:
        return False
    else:
        result = []
        for i in range(strk_1):
            new_strk = []
            for j in range(stlb_2):
                new_strk.append(0)
            result.append(new_strk)

        for i in range(strk_1):
            for j in range(stlb_2):
                summa = 0
                for k in range(stlb_1):
                    num_1 = matrix_1[i][k]
                    num_2 = matrix_2[k][j]
                    summa = summa + (num_1 * num_2)
                result[i][j] = summa

        for stroka in result:
            return stroka

print(mmatrix([
    [1, 2, 3]
], [
    [4],
    [5],
    [6]
]))