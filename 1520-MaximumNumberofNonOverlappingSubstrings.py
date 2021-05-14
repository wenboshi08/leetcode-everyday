class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:

        ranges = {c: (s.rindex(c), s.index(c)) for c in set(s)}

        for c in set(s):
            r, l = ranges[c]
            r_, l_ = -1, -1
            while not (r_ == r and l_ == l):
                r_, l_ = r, l
                r = max(ranges[c][0] for c in set(s[l:r + 1]))
                l = min(ranges[c][1] for c in set(s[l:r + 1]))
            ranges[c] = (r, l)

        ans = []
        curr = 0

        for r, l in sorted(ranges.values()):
            if l >= curr:
                ans.append(s[l:r + 1])
                curr = r
        return ans