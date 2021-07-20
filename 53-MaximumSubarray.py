class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        def divide_conquer(i, j):
            if i == j - 1:
                return nums[i], nums[i], nums[i], nums[i]
            # a which is max contiguous sum in nums[i:j] including the first value
            # m which is max contiguous sum in nums[i:j] anywhere 
            # b which is max contiguous sum in nums[i:j] including the last value
            # s which is the sum of all values in nums[i:j]
            mid = (i + j) // 2
            a1, m1, b1, s1 = divide_conquer(i, mid)
            a2, m2, b2, s2 = divide_conquer(mid, j)
            
            a = max(a1, s1+a2)
            b = max(b2, s2 + b1)
            m = max(m1, m2, b1+ a2)
            s = s1 + s2
            
            return a, m, b, s
        
        _, m, _, _ = divide_conquer(0, len(nums))
        return m
