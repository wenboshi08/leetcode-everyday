class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def valid(s):
            counter = 0
            for c in s:
                if c == '(':
                    counter += 1
                elif c == ')':
                    counter -= 1
                    if counter < 0:
                        return False
            return counter == 0

        if valid(s):
            return [s]
        queue = [s]
        res = set()
        while queue and len(res) == 0:
            next = set()
            for s in queue:
                n = len(s)
                for i in range(n):
                    new_s = s[:i] + s[i + 1:]
                    next.add(new_s)
                    if valid(new_s):
                        res.add(new_s)
            queue = next
        return list(res)