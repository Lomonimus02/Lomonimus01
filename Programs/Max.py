def maxx(nums):
    max_num = 0
    for i in nums:
        if i > max_num:
            max_num = i
    return max_num
print(maxx([2,244,4,1,6,0,1,9,2]))
'''эта программа ищет максимальный элемент списка'''