class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        total = 0
        for i in range(n):
            total += customers[i] * (1 - grumpy[i])
        res = total
        i = 0
        while i < n:
            if grumpy[i] == 1:
                total += customers[i]
            if i >= X and grumpy[i-X] == 1:
                total -= customers[i-X]
            res = max(res, total)
            i += 1
        return res