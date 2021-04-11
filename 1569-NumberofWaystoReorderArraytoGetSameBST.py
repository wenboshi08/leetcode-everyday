class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def ways_interleave(nums1, nums2):
            # split n slots to two shares
            # one share has len(nums1) slot, one has len(nums2) slots
            n = len(nums1) + len(nums2)
            m = len(nums1)
            return math.comb(n, m)

        def helper(nums):
            if not nums:
                return 1
            root_value = nums[0]
            left = [number for number in nums if number < root_value]
            right = [number for number in nums if number > root_value]
            ways_left = helper(left)
            ways_right = helper(right)
            return ways_left * ways_right * ways_interleave(left, right)

        return (helper(nums) - 1) % (10 ** 9 + 7)