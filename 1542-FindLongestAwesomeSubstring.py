class Solution:
    def longestAwesome(self, s: str) -> int:
        ans = 0
        mask = 0
        memo = [len(s)]*2**10
        memo[0] = -1
        for i, d in enumerate(s):
            mask ^= 1 << int(d)
            # Case 1: Check if we have seen similar mask
            ans = max(ans, i-memo[mask])
            # Case 2: Check for masks that differ by one bit
            for j in range(10):
                test_mask = mask^(1<<j)
                ans = max(ans, i-memo[test_mask])
            # save the earliest position
            memo[mask] = min(memo[mask], i)
        return ans
