def find_valid_partitions(numbers_str):
    numbers = [int(char) for char in numbers_str]
    valid_partitions = []

    for i in range(1, len(numbers)):
        left_part = numbers[:i]
        right_part = numbers[i:]

        left_part_str = ''.join(map(str, left_part))
        right_part_str = ''.join(map(str, right_part))

        if int(left_part_str) < int(right_part_str):
            valid_partitions.append(f"{left_part_str}\\{right_part_str}")

    return valid_partitions


numbers_str = input("Введи строку чисел без пробелов и запятых: ")
partitions = find_valid_partitions(numbers_str)
for partition in partitions:
    print(partition)



