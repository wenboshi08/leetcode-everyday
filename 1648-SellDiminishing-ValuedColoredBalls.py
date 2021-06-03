class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        
        inventory.sort(reverse=True)
        inventory = inventory + [0]
        i = 0
        n = len(inventory)
        
        def presum(x):
            return x*(1+x)//2
        
        res = 0
        while i < n-1 and orders > 0:
            gap = (i+1) *(inventory[i] - inventory[i+1])
            if gap <= orders:
                res += (i+1)*(presum(inventory[i])-presum(inventory[i+1]))
                orders -= gap
                i += 1
            else:
                x, y = divmod(orders, i+1)
                res += (i+1)*(presum(inventory[i])-presum(inventory[i]-x))
                res += y*(inventory[i]-x)
                break
        return res % (10**9+7)
