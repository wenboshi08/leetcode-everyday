class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.a = nums
        self.c = [0] * (self.n + 1)
        for i in range(len(nums)):
            self.add(i + 1, nums[i])

    def add(self, x, val):
        while x <= self.n:
            self.c[x] += val
            x += self.lowbit(x)

    def lowbit(self, x):
        return x & -x

    def presum(self, x):
        res = 0
        while x > 0:
            res += self.c[x]
            x -= self.lowbit(x)
        return res

    def update(self, index: int, val: int) -> None:
        self.add(index + 1, val - self.a[index])
        self.a[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.presum(right + 1) - self.presum(left)