class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        if len(nums) < 2 or min(nums) == max(nums):
            return 0
        a, b = min(nums), max(nums)
        size = math.ceil((b - a) / (len(nums) - 1))

        bucket = [[None, None] for _ in range((b - a) // size + 1)]

        for n in nums:
            b = bucket[(n - a) // size]
            b[0] = n if not b[0] else min(b[0], n)
            b[1] = n if not b[1] else max(b[1], n)
        bucket = [b for b in bucket if b[0]]
        return max((bucket[i][0] - bucket[i - 1][1]) for i in range(1, len(bucket)))