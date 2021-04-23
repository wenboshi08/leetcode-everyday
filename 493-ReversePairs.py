class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        def sort(low, high):
            if high - low < 2:
                return 0
            mid = (low + high) // 2
            count = sort(low, mid) + sort(mid, high)
            right_index = mid
            for left_val in nums[low:mid]:
                while right_index < high and nums[right_index] * 2 < left_val:
                    right_index += 1
                count += right_index - mid

            nums[low:high] = sorted(nums[low:high])
            return count

        return sort(0, len(nums))