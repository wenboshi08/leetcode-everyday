class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = collections.defaultdict(int)
        count[0] = 1
        res = 0
        presum = 0

        for n in nums:
            presum += n
            res += count[presum - goal]
            count[presum] += 1
        return res