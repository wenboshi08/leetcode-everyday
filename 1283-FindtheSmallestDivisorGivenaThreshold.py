class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left < right:
            mid = (left + right) // 2
            # check if mid satify the result
            cur_sum = sum([(i+mid-1)//mid for i in nums])
            if cur_sum > threshold:
                left = mid + 1
            else:
                right = mid
        return left