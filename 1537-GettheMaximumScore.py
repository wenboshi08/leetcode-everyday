class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = 0, 0
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0
        while i < n1 or j < n2:
            if j < n2 and (i == n1 or nums1[i] > nums2[j]):
                sum2 += nums2[j]
                j += 1
            elif i < n1 and (j == n2 or nums1[i] < nums2[j]):
                sum1 += nums1[i]
                i += 1
            else:
                sum1 = sum2 = max(sum1, sum2) + nums1[i]
                i += 1
                j += 1
        return max(sum1, sum2)%(10**9+7)
