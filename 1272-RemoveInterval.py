class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:

        n = len(intervals)
        i = 0
        res = []
        while i < n:
            start = intervals[i][0]
            end = intervals[i][1]
            if end <= toBeRemoved[0]:
                res.append([start, end])
            elif start >= toBeRemoved[1]:
                res.append([start, end])
            else:
                if start < toBeRemoved[0]:
                    res.append([start, toBeRemoved[0]])
                if end > toBeRemoved[1]:
                    res.append([toBeRemoved[1], end])
            i += 1
        return res