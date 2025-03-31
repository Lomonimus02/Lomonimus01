class Solution:
    def isValid(self, s: str) -> bool:
        count = 0
        ddd = []
        for i in s:
            if i == "(" or i == "[" or "{":
                ddd.append(i)
            elif i == ")" or i == "]" or i == "}":
                if i == ddd.pop(i):
                    count = 1
                else:
                    count = 0
        if count == 1:
            return True
        else:
            return False
