# 32ms/87.88%

import itertools

class Solution:
    def __init__(self):
        self.ans = ""

    def largestTimeFromDigits(self, A: List[int]) -> str:
        # get all indices
        values = list(itertools.permutations(A))

        for value in values:
            if self.validTime(value):
                self.validResult(value)

        return self.ans

    def validTime(self, value):
        if value[0] > 2:
            return False
        if value[0] == 2 and value[1] > 3:
            return False
        if value[2] >= 6:
            return False
        return True

    def validResult(self, value):
        value = "%d%d:%d%d" %(value[0], value[1], value[2], value[3])
        if self.ans == "":
            self.ans = value
            return
        else:
            if int(self.ans[:2]) < int(value[:2]):
                self.ans = value
                return
            if int(self.ans[:2]) == int(value[:2]) and int(self.ans[3:]) < int(value[3:]):
                self.ans = value

        