def minn(nums):
    min_num = nums[0]
    for i in nums:
        if i < min_num:
            min_num = i
    return min_num
print(minn([233, 5, 6]))
'''эта программа ищет минимальный элемент'''