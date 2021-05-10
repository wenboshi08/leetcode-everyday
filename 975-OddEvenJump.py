class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:

        n = len(arr)
        next_higher = [None] * n
        next_lower = [None] * n
        stack = []
        for num, i in sorted([num, i] for i, num in enumerate(arr)):
            while stack and stack[-1] < i:
                next_higher[stack.pop()] = i
            stack.append(i)

        stack = []
        for num, i in sorted([-num, i] for i, num in enumerate(arr)):
            while stack and stack[-1] < i:
                next_lower[stack.pop()] = i
            stack.append(i)

        odd = [0] * n
        even = [0] * n
        odd[-1] = 1
        even[-1] = 1
        for i in range(n - 2, -1, -1):
            if next_higher[i]:
                odd[i] = even[next_higher[i]]
            if next_lower[i]:
                even[i] = odd[next_lower[i]]
        return sum(odd)