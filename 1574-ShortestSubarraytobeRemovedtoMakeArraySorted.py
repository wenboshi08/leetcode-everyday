class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr) - 1
        while l < r and arr[l + 1] >= arr[l]:
            l += 1
        if l == len(arr) - 1:
            return 0

        while r > 0 and arr[r - 1] <= arr[r]:
            r -= 1
        toRemove = min(len(arr) - l - 1, r)

        j = r
        for i in range(l + 1):
            while j < len(arr) and arr[i] > arr[j]:
                j += 1
            if j == len(arr):
                break
            toRemove = min(toRemove, j - i - 1)

        return toRemove