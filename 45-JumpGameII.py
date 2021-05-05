class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        njumps = 0

        while r < len(nums) - 1:
            farthest = max([nums[i] + i for i in range(l, r + 1)])
            l = r + 1
            r = farthest
            njumps += 1

        return njumps