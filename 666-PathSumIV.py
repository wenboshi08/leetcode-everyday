class Solution:
    def pathSum(self, nums: List[int]) -> int:
        # key is (depth, position)
        # value is the all path sum from leaf to this position
        sums = collections.defaultdict(int)
        # key is (depth, position)
        # value is the path count from leaf to this position
        paths = collections.defaultdict(int)

        # bottom up approach
        for num in nums[::-1]:
            depth = num // 100
            pos = (num // 10) % 10
            val = num % 10
            paths[(depth, pos)] = max(1, paths[(depth + 1, pos * 2 - 1)] + paths[(depth + 1, pos * 2)])
            sums[(depth, pos)] = sums[(depth + 1, pos * 2 - 1)] + sums[(depth + 1, pos * 2)] + paths[(depth, pos)] * val
        return sums[(1, 1)]