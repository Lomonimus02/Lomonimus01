ishodnaya_matrix = [
    [1, 2, 6],
    [3, 4, 7]
]

if ishodnaya_matrix == None:
    m = 0
    n = 0
else:
    m = len(ishodnaya_matrix)
    if not ishodnaya_matrix[0]:
        n = 0
    else:
        n = len(ishodnaya_matrix[0])

vsego_elementov = m * n

new_rows = int(input())
new_cols = int(input())

if vsego_elementov > 0 and new_rows > 0 and new_cols > 0 and new_rows * new_cols == vsego_elementov:
    ploskiy_spisok = []
    for stroka in ishodnaya_matrix:
        for element in stroka:
            ploskiy_spisok.append(element)

    novaya_matrix = []
    index_elementa = 0
    for i in range(new_rows):
        novaya_stroka = []
        for j in range(new_cols):
            novaya_stroka.append(ploskiy_spisok[index_elementa])
            index_elementa += 1
        novaya_matrix.append(novaya_stroka)

    for stroka in novaya_matrix:
        print(stroka)
    print(novaya_matrix)

else:
    print(ishodnaya_matrix)