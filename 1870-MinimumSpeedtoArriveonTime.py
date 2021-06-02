class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        
        def arrive_time(speed):
            n = len(dist)
            return dist[-1] / speed + sum((dist[i] + speed - 1) // speed for i in range(n - 1))
        
        left = 1
        right = 10**7 + 1
        
        while left < right:
            mid = (left+right)//2
            if arrive_time(mid) > hour:
                left = mid + 1
            else:
                right = mid
        if left == 10**7 + 1:
            return -1
        return left
