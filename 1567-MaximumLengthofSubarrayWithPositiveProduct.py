class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        pos = neg = res = 0

        for num in nums:
            if num > 0:
                pos += 1
                neg = neg + 1 if neg > 0 else 0
            elif num < 0:
                pos, neg = neg + 1 if neg > 0 else 0, pos + 1
            else:
                pos = 0
                neg = 0
            res = max(res, pos)
        return res