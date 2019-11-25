import collections

# 464ms/30.03%
class RecentCounter:
    def __init__(self):
        self.count = []
        self.slow = 0
        self.fast = -1

    def ping(self, t: int) -> int:
        self.count.append(t)
        self.fast += 1
        while self.count[self.fast] - self.count[self.slow] > 3000:
            self.slow += 1
        return self.fast - self.slow + 1

# queue
# 408ms/53.25%
class RecentCounter1:
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while t > self.q[0] + 3000:
            self.q.popleft()
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)