def print_matrix(s):

    num_rows = len(s)
    num_cols = len(s[0])

    col_widths = [0] * num_cols
    for row in s:
        for j, element in enumerate(row):
            col_widths[j] = max(col_widths[j], len(str(element)))

    for row in s:
        formatted_row = ""
        for j, element in enumerate(row):
            formatted_row += str(element).rjust(col_widths[j]) + "  "
        print(formatted_row)



print(print_matrix([[0]*3]*3))