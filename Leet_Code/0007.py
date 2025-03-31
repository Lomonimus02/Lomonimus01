class Solution:
    def reverse(self, num: int) -> int:
        num_0 = num
        if num < 0:
            num = num * -1
        num = str(num)
        num = num[::-1]
        num = int(num)
        if num >= 2**31-1 or num <= -2**31:
            return 0
        if num_0 >= 0:
            return num
        else:
            return num * -1