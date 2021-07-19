class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums or sum(nums)%k != 0:
            return False
        N = len(nums)
        nums.sort(reverse=True)
        
        def dp(mask, cur, memo):
            if mask == 0:
                return cur == 0
            elif cur == 0:
                return dp(mask, sum(nums)//k, memo)
            if (mask, cur) not in memo:
                res = False
                for bit in range(N):
                    # check if bitth bit in the set
                    if mask & (1 << bit):
                        if nums[bit] > cur:
                            continue
                        # set ith bit
                        if dp(mask ^ (1 << bit), cur-nums[bit], memo):
                            res = True
                            break
                memo[(mask, cur)] = res
            return memo[(mask, cur)]
        
        return dp(2**N-1, sum(nums)//k, dict())
