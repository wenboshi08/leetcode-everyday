class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        lookup = {'a': 4, 'e': 3, 'i': 2, 'o': 1, 'u': 0}
        maxLen = 0
        prefix = {}
        prefix[0] = -1
        cur = 0
        for i, ch in enumerate(s):
            if ch in lookup:
                cur ^= (1 << lookup[ch])
            if cur in prefix:
                maxLen = max(maxLen, i - prefix[cur])
            else:
                prefix[cur] = i
        return maxLen