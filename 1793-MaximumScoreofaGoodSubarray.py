class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        max_score = -float('inf')
        left = k
        right = k
        cur_min = nums[k]
        while left >= 0 and right <= n - 1:
            cur_score = cur_min * (right - left + 1)
            if cur_score > max_score:
                max_score = cur_score
            if left == 0 and right == n - 1:
                break
            elif left == 0:
                right += 1
                cur_min = min(cur_min, nums[right])
            elif right == n - 1:
                left -= 1
                cur_min = min(cur_min, nums[left])
            elif nums[left - 1] > nums[right + 1]:
                left -= 1
                cur_min = min(cur_min, nums[left])
            elif nums[left - 1] < nums[right + 1]:
                right += 1
                cur_min = min(cur_min, nums[right])
            else:
                left -= 1
                right += 1
                cur_min = min(cur_min, nums[right])

        return max_score