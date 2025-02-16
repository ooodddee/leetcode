from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]]

        for n in intervals[1:]:
            last = res[-1]
            if n[0] <= last[1]:
                last[1] = max(last[1], n[1])
            else:
                res.append(n)
        return res