# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        graph = collections.defaultdict(list)

        def dfs(node):
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                dfs(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                dfs(node.right)

        dfs(root)

        res = []
        visited = set()

        def dfs2(node, d):
            if d < K:
                visited.add(node)
                for v in graph[node]:
                    if v not in visited:
                        dfs2(v, d + 1)
            else:
                res.append(node.val)

        dfs2(target, 0)
        return res