
# 36ms/84.78%
class Solution:
    def __init__(self):
        self.ans = []

    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        for query in queries:
            self.ans.append(self.matchOne(query, pattern))
        return self.ans
    
    def matchOne(self, query: str, pattern: str) -> bool:
        if len(query) < len(pattern):
            return False
        slow = 0
        for fast in range(len(query)):
            if slow == len(pattern):
                for i in range(fast, len(query)):
                    if 'A' <= query[i] and 'Z' >= query[i]:
                        return False
                return True
            if query[fast] == pattern[slow]:
                slow += 1
                continue
            else:
                if 'A' <= query[fast] and 'Z' >= query[fast]:
                    return False 
        if slow == len(pattern):
            return True
        else:
            return False
