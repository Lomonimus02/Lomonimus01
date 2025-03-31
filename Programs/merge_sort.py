def sort_numbers(nums):

    if len(nums) <= 1:
        return nums

    pivot = nums[0]
    less = []
    equal = []
    greater = []

    for x in nums:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)

    return sort_numbers(less) + equal + sort_numbers(greater)


user_input = input("Введи числа через пробел: ")

numbers = [int(x) for x in user_input.split()]
sorted_numbers = sort_numbers(numbers)
print("Отсортировано:", sorted_numbers)