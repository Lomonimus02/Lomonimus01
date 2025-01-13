class Solution:
    def isPalindrome(self, x: int) -> bool:
       x = str(x)
       n = x[::-1]
       if n == x:
           return True
       else:
           return False

    def isPalindrome(self, x: int) -> bool:
        x = x%10
