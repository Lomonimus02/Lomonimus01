def find_valid_partitions(numbers):
    numbers = str(numbers)
    n = 0
    for i in range(len(numbers) // 2 - 1 + len(numbers) % 2):
        if numbers[i] != '0':
            n += 1
    if len(numbers) % 2 == 0 and numbers[:len(numbers) // 2:] <= numbers[len(numbers) // 2::]:
        n += 1
    return n

print(find_valid_partitions(10100))