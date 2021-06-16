class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        presum = [0]
        n = len(nums)
        for i in range(n):
            presum.append(presum[-1]+nums[i])
        res = 0
        
        stack = [-1]
        for i in range(n):
            while len(stack) > 1 and nums[stack[-1]] > nums[i]:
                j = stack.pop()
                res = max(res, nums[j]*(presum[i]-presum[stack[-1]+1]))
            stack.append(i)
        while len(stack) > 1:
            j = stack.pop()
            res = max(res, nums[j]*(presum[n]-presum[stack[-1]+1]))
        return res % (10**9+7)
