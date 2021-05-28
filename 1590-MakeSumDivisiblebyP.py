class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        target_mod = sum(nums) % p
        presum = 0
        pre = {0: -1}
        res = n

        for i, num in enumerate(nums):
            presum += num
            pre[presum % p] = i
            need_mod = (presum % p - target_mod) % p
            if need_mod in pre:
                res = min(res, i - pre[need_mod])
        if res == n:
            return -1
        return res