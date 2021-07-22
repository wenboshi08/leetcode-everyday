class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        m = 2*n-1
        A, V = [0] * m, [False] * (n+1)
        def dfs(i):
            if i == m:
                return all(A)
            if A[i]:
                return dfs(i+1)
            for x in range(n, 0, -1):
                j = i if x == 1 else i+x    # This is only to combine some lines of code.
                if not V[x] and j < m and not A[j]:
                    A[i], A[j], V[x] = x, x, True
                    if dfs(i+1):
                        return True
                    A[i], A[j], V[x] = 0, 0, False
            return False
        dfs(0)
        return A
