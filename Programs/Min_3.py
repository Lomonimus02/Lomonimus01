def min_3(nums):
    a1, a2, a3 = nums[0], nums[0], nums[0]
    a1 = nums[len(nums)-1]

    for i in range(len(nums)):
        if nums[i] <= a1:
            a3 = a2
            a2 = a1
            a1 = nums[i]
        elif a2 <= nums[i] > a1:
            a3 = a2
            a2 = nums[i]
        elif a3 <= nums[i] > a2:
            a3 = nums[i]
    return a3
print(min_3([1, 2, 3, 4, 5, 6, 7, 8, 9, 1]))
'''эта программа ищет 3 минимальный элемент'''
