class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right)//2
            cur = 0
            need = 0
            for w in weights:
                if cur < w:
                    cur = mid
                    need += 1
                cur -= w
            if need > D:
                left = mid + 1
            else:
                right = mid
        return left