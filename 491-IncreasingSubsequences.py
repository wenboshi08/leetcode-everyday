class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = set()
        
        def dfs(start, path, res):
            if len(path) >= 2:
                res.add(tuple(path[:]))
            for i in range(start, len(nums)):
                if not path or path[-1] <= nums[i]:
                    dfs(i+1, path+[nums[i]], res)
        dfs(0, [], res)
        return res
