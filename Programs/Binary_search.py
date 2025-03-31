def binary_search(nums, target):
    mid = int(len(nums)/2) -1
    stop = int(len(nums)) - 1
    while nums[mid] != target:
        if mid == stop:
            return None
        elif nums[mid] > target:
            stop = mid
            mid = int(mid/2)
        elif nums[mid] < target:
            mid = int((mid+1 + stop)/2)
    return mid
print(binary_search((1,2,3,4,5,6,7,8,9), 5))
'''эта программа выполняет бинарный поиск числа в списке'''