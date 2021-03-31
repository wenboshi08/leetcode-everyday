class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            hours = 0
            for p in piles:
                a, b = divmod(p, mid)
                hours += a
                if b > 0:
                    hours += 1
            if hours > h:
                left = mid + 1
            else:
                right = mid
        return left