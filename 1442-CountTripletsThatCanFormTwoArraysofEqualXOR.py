class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0

        curXOR = 0
        count = {0: [1, 0]}

        for i, num in enumerate(arr):
            curXOR ^= num
            n, total = count.get(curXOR, [0, 0])
            res += i * n - total
            count[curXOR] = [n + 1, total + i + 1]

        return res