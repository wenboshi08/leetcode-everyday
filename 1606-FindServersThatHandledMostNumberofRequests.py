class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = list(range(k))
        busy = []
        res = [0]*k
        for i, start in enumerate(arrival):
            while busy and busy[0][0] <= start:
                _, x = heapq.heappop(busy)
                heapq.heappush(available, i+(x-i)%k)
            if available:
                j = heapq.heappop(available)%k
                heapq.heappush(busy, (start+load[i], j))
                res[j] += 1
        a = max(res)
        return [i for i in range(k) if res[i]==a]
