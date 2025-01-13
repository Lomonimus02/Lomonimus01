class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return[i,j]
class Solution:
    def twoSum(self, nums, target: int):
        nums = {}
        for i in nums:
            for j in nums):
                if nums[i] + nums[j] == target and i != j:

