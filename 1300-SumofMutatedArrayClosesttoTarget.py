class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        arr.sort()
        n = len(arr)
        presum = [0]
        for i in range(n):
            presum.append(arr[i]+presum[-1])
        
        def binary_search(val):
            left = 0
            right = n
            while left < right:
                mid = (left+right)//2
                if arr[mid] < val:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def new_sum(mid):
            index = binary_search(mid)
            return presum[index] + (n-index)*mid
        
        left = 0
        right = arr[-1]
        while left < right - 1:
            mid = (left+right)//2
            sum_val = new_sum(mid)
            if sum_val < target:
                left = mid
            elif sum_val > target:
                right = mid
            else:
                return mid
        d_left = abs(target - new_sum(left))
        d_right = abs(target - new_sum(right))
        if d_left <= d_right:
            return left
        return right
