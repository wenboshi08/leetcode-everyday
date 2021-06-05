class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)
        left = 1
        right = position[-1] - position[0] + 1
        
        def placeballs(force):
            res = 1
            cur = 0
            for i in range(1, n):
                cur += position[i] - position[i-1]
                if cur >= force:
                    res += 1
                    cur = 0
            return res
            
        
        while left < right:
            mid = (left+right+1)//2
            if placeballs(mid) < m:
                right = mid - 1
            else:
                left = mid
        return left
