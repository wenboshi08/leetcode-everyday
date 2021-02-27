class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        queries = sorted(enumerate(queries), key=lambda x: x[1][1])
        trie = Trie()
        ans = [-1] * len(queries)
        j = 0
        for i, (x, m) in queries:
            while j < len(nums) and nums[j] <= m:
                trie.insert(nums[j])
                j += 1
            ans[i] = trie.query(x)
        return ans


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, num):
        p = self.root
        for i in range(31, -1, -1):
            # get the digit in corresponding position
            cur = (num >> i) & 1
            if cur not in p:
                p[cur] = {}
            p = p[cur]

    def query(self, num):
        if not self.root:
            return -1

        p = self.root
        res = 0
        for i in range(31, -1, -1):
            cur = (num >> i) & 1
            if 1 - cur in p:
                p = p[1 - cur]
                res |= (1 << i)
            else:
                p = p[cur]
        return res