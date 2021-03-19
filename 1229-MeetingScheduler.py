class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots = slots1 + slots2
        import heapq
        heapq.heapify(slots)
        while len(slots) > 1:
            pre = heapq.heappop(slots)
            if min(pre[1], slots[0][1]) - slots[0][0] >= duration:
                return [slots[0][0], slots[0][0] + duration]
        return []