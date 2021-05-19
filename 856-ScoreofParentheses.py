class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        cur = 0
        for c in s:
            if c == "(":
                stack.append(cur)
                cur = 0
            else:
                cur += max(cur, 1)
                cur += stack.pop()
        return cur