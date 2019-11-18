
# 200ms/6.45%
class RLEIterator:
    def __init__(self, A: List[int]):
        times = []
        nums = []
        for i in range(len(A)):
            if i % 2 == 0:
                times.append(A[i])
            else:
                nums.append(A[i])
        self.times = times
        self.nums = nums

    def next(self, n: int) -> int:
        for i in range(len(self.nums)):
            if self.times[i] < n:
                n -= self.times[i]
                self.times[i] = 0
                continue
            else:
                self.times[i] -= n
                return self.nums[i]
        return -1

# 2nd edition
# 44ms/93.55%
class RLEIterator1:
    def __init__(self, A: List[int]):
        self.rle = A
        self.i = 0
        self.q = 0
        self.flag = True

    def next(self, n: int) -> int:
        while self.flag and (self.rle[self.i] - self.q) < n:
            n -= (self.rle[self.i] - self.q)
            self.i += 2
            self.q = 0
            if self.i == len(self.rle):
                self.flag = False
                break
        if self.flag:
            self.q += n
            return self.rle[self.i+1]
        else:
            return -1

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)