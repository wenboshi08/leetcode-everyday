class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = [float('inf')]
        
        for a in arr:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid*min(stack[-1], a)
            stack.append(a)
        
        while len(stack) > 2:
            mid = stack.pop()
            res += mid*stack[-1]
        
        return res
