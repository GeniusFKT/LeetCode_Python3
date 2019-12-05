
# 36ms/94.95%
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for symbol in s:
            if symbol == "(" or symbol == "[" or symbol == "{":
                stack.append(symbol)
            else:
                if stack == []:
                    return False
                char = stack.pop()
                if ord(symbol) - ord(char) < 1 or ord(symbol) - ord(char) > 2:
                    return False
        if stack == []:
            return True
        else:
            return False