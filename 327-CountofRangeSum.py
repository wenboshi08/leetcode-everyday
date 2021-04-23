class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)

        def sort(lo, hi):
            if lo + 1 == hi:
                return 0
            mid = (lo + hi) // 2
            count = sort(lo, mid) + sort(mid, hi)
            i = j = mid
            for left in preSum[lo:mid]:
                while i < hi and preSum[i] - left < lower:
                    i += 1
                while j < hi and preSum[j] - left <= upper:
                    j += 1
                count += j - i
            preSum[lo:hi] = sorted(preSum[lo:hi])
            return count

        return sort(0, len(preSum))