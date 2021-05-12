class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        premax = nums[0]
        right = 0
        for i in range(n):
            premax = max(premax, nums[i])
            if nums[i] < premax:
                right = i
        if right == 0:
            return 0

        postmin = nums[n - 1]
        left = n - 1
        for i in range(n - 1, -1, -1):
            postmin = min(postmin, nums[i])
            if nums[i] > postmin:
                left = i
        return right - left + 1