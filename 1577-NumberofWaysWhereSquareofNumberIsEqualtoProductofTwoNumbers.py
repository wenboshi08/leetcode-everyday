class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = collections.Counter(nums1)
        n2 = collections.Counter(nums2)

        res = 0

        for i in range(len(nums1) - 1):
            for j in range(i + 1, len(nums1)):
                t = (nums1[i] * nums1[j]) ** (1 / 2)
                if t == int(t) and t in n2:
                    res += n2[t]

        for i in range(len(nums2) - 1):
            for j in range(i + 1, len(nums2)):
                t = (nums2[i] * nums2[j]) ** (1 / 2)
                if t == int(t) and t in n1:
                    res += n1[t]

        return res