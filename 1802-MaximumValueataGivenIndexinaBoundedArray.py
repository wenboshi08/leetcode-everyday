class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        
        def min_sum(target, index):
            left_index = index-target+1
            right_index = target+index-1
            left = 0
            right = 0
            if left_index >= 0:
                left = target*(target+1)//2 + left_index
            else:
                left = (2*target - index)*(index+1)//2
            if right_index <= n-1:
                right = target*(target+1)//2 + n-1-right_index
            else:
                right = (2*target -n +1+index)*(n-index)//2
            return left+right-target
        
        left = 1
        right = maxSum + 1
        while left < right:
            mid = (left+right+1)//2
            if min_sum(mid, index)>maxSum:
                right = mid - 1
            else:
                left = mid
        return left
