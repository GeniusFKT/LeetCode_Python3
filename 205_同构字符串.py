
# 64ms/41.2%
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m = {}
        n = {}
        for idx in range(len(s)):
            if m.get(s[idx]) is None:
                m[s[idx]] = t[idx]
            else:
                if m[s[idx]] != t[idx]:
                    return False
            if n.get(t[idx]) is None:
                n[t[idx]] = s[idx]
            else:
                if n[t[idx]] != s[idx]:
                    return False

        return True
