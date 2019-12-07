# 36ms/94.52%
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        s = 0
        while num >= 10:
            s += num % 10
            num /= 10
        return self.addDigits(s + num)

class Solution1:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        a = num % 9
        if a == 0:
            return 9
        else:
            return a