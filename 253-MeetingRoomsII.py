class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])
        n = len(intervals)
        max_rooms = 0
        i = 0
        for j in range(n):
            while i < n and start[i] < end[j]:
                i += 1
            max_rooms = max(i-j, max_rooms)
        return max_rooms