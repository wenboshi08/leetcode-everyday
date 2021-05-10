class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        import functools
        compare = lambda a, b: -1 if a+b > b+a else 1 if a+b < b+a else 0
        _nums = list(map(str, nums))
        _nums.sort(key = functools.cmp_to_key(compare))
        return str(int(''.join(_nums)))