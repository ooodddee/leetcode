class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for n in intervals:
            if n[1] < newInterval[0]:
                res.append(n)
            elif n[0] > newInterval[1]:
                res.append(newInterval)
                res.extend(intervals[intervals.index(n):])
                return res
            else:
                newInterval[0] = min(n[0], newInterval[0])
                newInterval[1] = max(n[1], newInterval[1])
        res.append(newInterval)
        return res


# interate throught the array:
#     1.append: if end < new's start
#     2. extend: elif start > new's end: res.extend
#     2.else: 
#     start = 
#         start = min()
#         end = max()

