class Solution:
    def longestValidParentheses(self, s: str) -> int:

        n = len(s)
        stack = []

        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    stack.append(i)

        stack = [-1] + stack + [n]
        max_len = 0

        for i in range(len(stack) - 1):
            max_len = max(stack[i + 1] - stack[i] - 1, max_len)

        return max_len