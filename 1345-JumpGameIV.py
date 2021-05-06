class Solution:
    def minJumps(self, arr: List[int]) -> int:
        nei = collections.defaultdict(list)
        for i, x in enumerate(arr):
            nei[x].append(i)

        frontier = collections.deque([(0, 0)])
        pos_met = {0}
        while frontier:
            pos, step = frontier.popleft()  # state: position, step
            if pos == len(arr) - 1:
                return step
            num = arr[pos]

            for p in [pos - 1, pos + 1] + nei[num]:
                if p not in pos_met and 0 <= p < len(arr):
                    frontier.append((p, step + 1))
                    pos_met.add(p)
            del nei[num]