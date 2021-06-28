class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        i = 0
        freq1 = encoded1[i][1]
        val1 = encoded1[i][0]
        n = len(encoded1)
        res = []
        for val2, freq2 in encoded2:
            while freq2 > 0:
                cur_val = val1*val2
                if freq2 >= freq1:
                    if len(res) == 0 or res[-1][0] != cur_val:
                        res.append([cur_val, freq1])
                    else:
                        res[-1][1] += freq1
                    freq2 -= freq1
                    i += 1
                    if i < n:
                        freq1 = encoded1[i][1]
                        val1 = encoded1[i][0]
                else:
                    if len(res) == 0 or res[-1][0] != cur_val:
                        res.append([cur_val, freq2])
                    else:
                        res[-1][1] += freq2
                    freq1 -= freq2
                    freq2 = 0
        return res
