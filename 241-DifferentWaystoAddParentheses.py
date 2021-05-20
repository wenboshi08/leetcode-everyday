class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        if expression.isdigit():
            return [int(expression)]

        res = []
        for i in range(len(expression)):
            if expression[i] in '-+*':
                res1 = self.diffWaysToCompute(expression[:i])
                res2 = self.diffWaysToCompute(expression[i + 1:])
                res += [eval(str(k) + expression[i] + str(j)) for k in res1 for j in res2]
        return res
