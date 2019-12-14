
# 36ms/90.52%
class Solution:
    def __init__(self):
        self.ans = ""

    def reverseWords(self, s: str) -> str:
        def _reverseWords(s):
            s = s.lstrip()
            if s == "":
                return ""
            idx = s.find(" ")
            if idx == -1:
                self.ans = s + " " + self.ans
            else:
                self.ans = s[:idx] + " " + self.ans
                _reverseWords(s[idx:])
        _reverseWords(s)
        return self.ans.lstrip().rstrip()