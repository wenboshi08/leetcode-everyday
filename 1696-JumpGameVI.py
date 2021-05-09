class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:

        # dp(i) the maximum score when reaching i from 0
        n = len(nums)
        dp = [-float('inf')] * n
        dp[0] = nums[0]
        # maintain a value decreasing order deque
        deque = collections.deque([(dp[0], 0)])
        for i in range(1, n):
            while deque[0][1] < i - k:
                deque.popleft()
            dp[i] = nums[i] + deque[0][0]
            while deque and dp[i] >= deque[-1][0]:
                deque.pop()
            deque.append((dp[i], i))
        return dp[-1]