class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        nums = nums + [-math.inf]
        stack = []
        n = len(nums)
        res = 0
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] > num:
                res += (i-stack.pop())
            stack.append(i)
        return res
