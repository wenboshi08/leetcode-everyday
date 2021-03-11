class MyCalendarThree:

    def __init__(self):
        self.delta = collections.Counter()

    def book(self, start: int, end: int) -> int:
        self.delta[start] += 1
        self.delta[end] -= 1
        active = ans = 0
        for x in sorted(self.delta):
            active += self.delta[x]
            if active > ans:
                ans = active
        return ans