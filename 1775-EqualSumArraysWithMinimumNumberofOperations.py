class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        import heapq
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        res = 0
        if sum1 == sum2:
            return res
        if sum1 > sum2:
            nums2, nums1 = nums1, nums2
            sum1, sum2 = sum2, sum1
        gap = sum2 - sum1
        gains = [x-6 for x in nums1] + [1-x for x in nums2]
        heapq.heapify(gains)
        while gains:
            gap -= min(gap, -gains[0])
            heapq.heappop(gains)
            res += 1
            if gap == 0:
                return res
        return -1
