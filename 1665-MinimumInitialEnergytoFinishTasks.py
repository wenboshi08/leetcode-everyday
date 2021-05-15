class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:

        tasks.sort(key=lambda x: x[0] - x[1])
        ans = 0
        cur = 0
        for cost, start in tasks:
            if start > cur:
                ans += start - cur
                cur = start
            cur -= cost
        return ans