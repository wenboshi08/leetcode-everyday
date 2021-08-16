class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        @lru_cache(None)
        def dp(i, k):
            if k < 0:
                return float('inf')
            if i < 0:
                return 0
            return dist[i] + min(dp(i-1, k-1), (dp(i-1, k) + speed-1)//speed*speed)
        
        n = len(dist)
        for k in range(n+1):
            if dp(n-1, k) <= hoursBefore*speed:
                return k
        return -1
