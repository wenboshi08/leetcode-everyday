class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:

        def possible(D):
            count = 0
            for a, b in zip(stations, stations[1:]):
                count += int((b - a) / D)
            return count <= k

        left = 0
        right = stations[-1] - stations[0]
        while right - left > 1e-6:
            mid = (left + right) / 2
            if possible(mid):
                right = mid
            else:
                left = mid
        return left