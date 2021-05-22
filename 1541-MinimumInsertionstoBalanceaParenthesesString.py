class Solution:
    def minInsertions(self, s: str) -> int:

        open_p = 0

        # open and close already added
        res = 0

        n = len(s)
        i = 0
        while i < n:
            if s[i] == '(':
                open_p += 1
                i += 1
            elif i < n - 1 and s[i] == ')' and s[i + 1] == ")":
                if open_p > 0:
                    open_p -= 1
                else:
                    res += 1
                i += 2
            else:
                if open_p > 0:
                    res += 1
                    open_p -= 1
                else:
                    res += 2
                i += 1
        res += 2 * open_p
        return res