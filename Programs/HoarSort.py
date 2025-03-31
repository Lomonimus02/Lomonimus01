def sort_numbers(nums):

    if len(nums) <= 1:
        print("Готово:", nums)
        return

    def quicksort(low, high):

        if low < high:
            pivot = nums[low]
            i = low - 1
            j = high + 1

            while True:
                i += 1
                while nums[i] < pivot:
                    i += 1

                j -= 1
                while nums[j] > pivot:
                    j -= 1

                if i >= j:
                    break

                nums[i], nums[j] = nums[j], nums[i]

            quicksort(low, j)
            quicksort(j + 1, high)

    quicksort(0, len(nums) - 1)
    print("Отсортировано:", nums)


user_input = input("Введи числа через пробел: ")

numbers = [int(x) for x in user_input.split()]
sort_numbers(numbers)