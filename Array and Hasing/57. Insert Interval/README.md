## 57. Insert Interval
<https://leetcode.com/problems/insert-interval/>


=======================================================================================<br>

### UMPIRE Method:
#### Understand


1. Empty? Return [newInterval]
2. sorted:
    * no
    

### Match

1. Sorting and merging overlaps
    1. Add all intervals that come before newInterval
    2. Merge overlapping intervals with newInterval
    3. Add all intervals that come after newInterval


### Plan
1. Initialize an empty result list res
2. Traverse the intervals array:
    1. If the current interval ends before newInterval starts, add it to res
    2. If the current interval starts after newInterval ends , add newInterval to res
    3. If the current interval overlaps with newInterval, merge them by updating newInterval
3. If newInterval hasn’t been added, add it to res
4. Return res

### Implement

see solution.py

### Review

### Evaluate

- Time Complexity: O(N), iterate the entire intervals
    
- Space Complexity: need a new res list to sort the result
    