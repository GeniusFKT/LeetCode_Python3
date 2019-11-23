
# 32ms/98.63%
class Solution:
    def countSegments(self, s: str) -> int:
        count = 0
        flag = True
        for i in s:
            if i == " ":
                flag = True
            else:
                if flag:
                    count += 1
                    flag = False
                