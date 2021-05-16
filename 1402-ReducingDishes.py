class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        n = len(satisfaction)
        presum = [satisfaction[0]]
        for i in range(1, n):
            presum.append(presum[-1] + satisfaction[i])
        res = 0
        cur_s = 0
        for i in range(n):
            cur_s = cur_s + presum[i]
            if cur_s > 0:
                res = max(res, cur_s)
            else:
                break
        return res