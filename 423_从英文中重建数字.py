
# 100ms/18.52%
class Solution:
    def originalDigits(self, s: str) -> str:
        count = {}
        for i in s:
            if count.get(i) is None:
                count[i] = 1
            else:
                count[i] += 1

        count_digit = [0 for _ in range(10)]
        if count.get('z') is not None:
            count_digit[0] = count['z']
            count['o'] -= count['z']
        if count.get('w') is not None:
            count_digit[2] = count['w']
            count['o'] -= count['w']
        if count.get('u') is not None:
            count_digit[4] = count['u']
            count['o'] -= count['u']
            count['f'] -= count['u']
        if count.get('f') is not None:
            count_digit[5] = count['f']
            if count.get('v') is not None:
                count['v'] -= count['f']
        if count.get('o') is not None:
            count_digit[1] = count['o']
            if count.get('n') is not None:
                count['n'] -= count['o']
        if count.get('x') is not None:
            count_digit[6] = count['x']
        if count.get('v') is not None:
            count_digit[7] = count['v']
            if count.get('n') is not None:
                count['n'] -= count['v']
        if count.get('g') is not None:
            count_digit[8] = count['g']
            count['h'] -= count['g']
        if count.get('h') is not None:
            count_digit[3] = count['h']
        if count.get('n') is not None:
            count_digit[9] = count['n'] // 2

        ans = ""
        for num in range(len(count_digit)):
            for _ in range(count_digit[num]):
                ans += "%d" %(num)
        return ans


        

        