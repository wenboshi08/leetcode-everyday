class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n
        # left close, right open
        # find the first index where citations[i] >= n - i
        while left < right:
            mid = (left+right)//2
            if citations[mid] < n - mid:
                left = mid + 1
            else:
                right = mid
        # convert the index to h-index
        return n - left