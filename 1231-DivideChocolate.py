class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        left = min(sweetness)
        right = sum(sweetness) + 1

        def fail(mid):
            pieces = 0
            cursum = 0
            for sweet in sweetness:
                cursum += sweet
                if cursum >= mid:
                    pieces += 1
                    cursum = 0
            return pieces < K + 1

        while left < right:
            mid = (left + right) // 2
            if fail(mid):
                right = mid
            else:
                left = mid + 1
        return left - 1