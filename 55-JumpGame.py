class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = 0
        r = 0
        n = len(nums)
        while True:
            nr = max([nums[i] + i for i in range(l, r + 1)])
            nl = l + 1

            if nr >= n - 1:
                return True
            if nr == r:
                return False
            r, l = nr, nl