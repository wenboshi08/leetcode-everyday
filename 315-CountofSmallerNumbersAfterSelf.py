class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        hashTable = {v: i for i, v in enumerate(sorted(set(nums)))}

        tree = BinaryIndexedTree(len(hashTable))
        res = []
        for i in range(len(nums) - 1, -1, -1):
            res.append(tree.sum(hashTable[nums[i]]))
            tree.update(hashTable[nums[i]] + 1, 1)
        return res[::-1]


class BinaryIndexedTree:
    def __init__(self, n):
        self.sums = [0] * (n + 1)

    def update(self, i, val):
        while i < len(self.sums):
            self.sums[i] += val
            i += i & - i

    def sum(self, i):
        r = 0
        while i > 0:
            r += self.sums[i]
            i -= i & - i
        return r