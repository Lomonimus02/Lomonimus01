def decompose_and_print_recursive(n, seen=None):
    if seen is None:
        seen = set()

    if n == 1:
        print(f"{' + '.join(f'{d}**2' for d in str(n))} = {n}")
        return

    if n in seen:
        print("Цикл обнаружен.")
        return

    seen.add(n)
    digits = []
    temp = n
    while temp > 0:
        digits.insert(0, temp % 10)
        temp //= 10

    expression = " + ".join(f"{d}**2" for d in digits)
    next_val = sum(d * d for d in digits)
    print(f"{expression} = {next_val}")

    decompose_and_print_recursive(next_val, seen)


def main():
    try:
        n = int(input("Введите целое число: "))
        if n <= 0:
            print("Пожалуйста, введите положительное целое число.")
            return

        decompose_and_print_recursive(n)

    except ValueError:
        print("Ошибка: Введите целое число.")


if __name__ == "__main__":
    main()