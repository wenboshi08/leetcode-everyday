class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k > len(bloomDay):
            return -1
        left = min(bloomDay)
        right = max(bloomDay)
        while left < right:
            mid = (left + right) // 2
            # find the M satify the k condition
            flow = bouq = 0
            for a in bloomDay:
                # reset flow to 0 if current flow not bloom yet
                flow = 0 if a > mid else flow + 1
                if flow == k:
                    flow = 0
                    bouq += 1
                    if bouq == m: break
            if bouq == m:
                right = mid
            else:
                left = mid + 1
        return left