class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        ans = [0]
        
        def dfs(index, visited):
            if index == n:
                ans[0] = max(len(visited), ans[0])
                return
            for j in range(index+1, n+1):
                if s[index:j] in visited:
                    continue
                visited.add(s[index:j])
                dfs(j, visited)
                visited.remove(s[index:j])
        
        dfs(0, set())
        return ans[0]
