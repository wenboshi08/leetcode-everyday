class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(l, -h, r) for l, r, h in buildings] + [(r, 0, 0) for l, r, h in buildings]
        events.sort()

        # (event_start, height)
        res = [(0, 0)]
        # (height, event_end)
        heap = [(0, float('inf'))]
        import heapq

        for l, h, r in events:
            # pop out the expired event
            while l >= heap[0][1]:
                heapq.heappop(heap)
            # insert the new event to heap
            if h:
                heapq.heappush(heap, (h, r))
            # determine if new key point is found
            if res[-1][1] != -heap[0][0]:
                res.append([l, -heap[0][0]])
        return res[1:]