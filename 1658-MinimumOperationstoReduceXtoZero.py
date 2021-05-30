class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        target = total - x

        pre = {0: -1}
        presum = 0
        res = math.inf
        for i, num in enumerate(nums):
            presum += num
            pre[presum] = i
            need = presum - target
            if need in pre:
                res = min(res, n - i + pre[need])
        return -1 if res == math.inf else res