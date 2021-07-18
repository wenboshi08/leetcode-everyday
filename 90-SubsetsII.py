class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        
        def backtrack(index, path, res):
            if index == n:
                res.append(path[:])
                return
            path.append(nums[index])
            backtrack(index + 1, path, res)
            path.pop()
            start = index + 1
            while start < n and nums[start] == nums[index]:
                start += 1
            backtrack(start, path, res)
            
            
                    
        res = []
        backtrack(0, [], res)
        return res
