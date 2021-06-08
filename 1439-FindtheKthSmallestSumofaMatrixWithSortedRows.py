class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        n = len(mat)
        m = len(mat[0])
        
        s = 0
        for i in range(n):
            s += mat[i][0]
        
        queue = [(s, tuple([0 for _ in range(n)]))]
        visited = set(tuple([0 for i in range(n)]))
        import heapq
        while k > 0:
            sm, tup = heapq.heappop(queue)
            if k == 1:
                return sm
            k -= 1
            l = list(tup)
            for i in range(n):
                l[i] += 1
                if l[i] < m and tuple(l) not in visited:
                    heapq.heappush(queue, (sm - mat[i][l[i] -1] + mat[i][l[i]], tuple(l)))
                    visited.add(tuple(l))
                l[i] -= 1
