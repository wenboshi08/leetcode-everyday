class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        
        def valid(sweet):
            pieces = 0
            cur_sweet = 0
            for s in sweetness:
                cur_sweet += s
                if cur_sweet >= sweet:
                    pieces += 1
                    cur_sweet = 0
            return pieces >= K + 1
        
        left = min(sweetness)
        right = sum(sweetness)
        
        while left < right:
            mid = (left+right + 1)// 2
            if valid(mid):
                left = mid
            else:
                right = mid - 1
        return left
