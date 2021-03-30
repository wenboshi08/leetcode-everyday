class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:

        l, r = max(nums), sum(nums)

        while l < r:
            mid = (l + r) // 2
            count, cur = 1, 0
            for n in nums:
                cur += n
                if cur > mid:
                    count += 1
                    cur = n
            if count > m:
                l = mid + 1
            else:
                r = mid
        return l