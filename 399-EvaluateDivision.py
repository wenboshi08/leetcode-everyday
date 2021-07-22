class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for e, v in zip(equations, values):
            s = e[0]
            e = e[1]
            graph[s][e] = v
            graph[e][s] = 1/v
            
        
        def dfs(start, end, visited, cur_v):
            
            if start == end:
                return cur_v
            
            for nb in graph[start].keys():
                if nb not in visited:
                    visited.add(nb)
                    res = dfs(nb, end, visited, cur_v * graph[start][nb])
                    if res:
                        return res
                    visited.remove(nb)
        res = []
        for q in queries:
            if q[0] not in graph or q[1] not in graph:
                res.append(-1.0)
            else:
                cur = dfs(q[0], q[1], {q[0]}, 1.0)
                if cur:
                    res.append(cur)
                else:
                    res.append(-1.0)
        return res
