class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n = len(firstList)
        m = len(secondList)
        res = []
        i = 0
        j = 0
        while i < n and j < m:
            low = max(firstList[i][0], secondList[j][0])
            high = min(firstList[i][1], secondList[j][1])
            if low <= high:
                res.append([low, high])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return res
