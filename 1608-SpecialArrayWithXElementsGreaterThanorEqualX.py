class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)//2
            if mid < nums[mid]:
                left = mid + 1
            else:
                right = mid
        if left < len(nums) and left == nums[left]:
            return -1
        return left
