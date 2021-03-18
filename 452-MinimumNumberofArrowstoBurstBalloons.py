class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        count = 0
        arrow = -float('inf')
        for p in points:
            if p[0] > arrow:
                count += 1
                arrow = p[1]
        return count