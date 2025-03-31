def max_3(nums):
    a1, a2, a3 = 0, 0, 0
    a1 = nums[0]

    for i in range(len(nums)):
        if nums[i] >= a1:
            a3 = a2
            a2 = a1
            a1 = nums[i]
        elif nums[i] >= a2:
            a3 =a2
            a2 = nums[i]
        elif nums[i] >= a3:
            a3 = nums[i]
    return a3
print(max_3([2,244,4,1,6,0,1,9,2]))
'''эта программа ищет третий максимальный элемент'''