class Solution:
    def checkValidString(self, s: str) -> bool:
        open_min = open_max = 0

        for c in s:
            open_min = open_min + 1 if c == "(" else max(open_min - 1, 0)
            open_max = open_max - 1 if c == ")" else open_max + 1
            if open_max < 0:
                return False
        return open_min == 0