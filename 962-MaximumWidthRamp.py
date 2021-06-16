class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        s = []
        res = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if not s or nums[s[-1]] > num:
                s.append(i)
        for j in range(n-1, -1, -1):
            while s and nums[s[-1]] <= nums[j]:
                res = max(res, j - s.pop())
        return res
