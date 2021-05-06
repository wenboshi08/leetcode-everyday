class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()

        def helper(index):
            if arr[index] == 0:
                return True
            visited.add(index)
            res = False
            if index + arr[index] < n and (index + arr[index]) not in visited:
                res = res or helper(index + arr[index])
            if index - arr[index] >= 0 and (index - arr[index]) not in visited:
                res = res or helper(index - arr[index])
            return res

        return helper(start)