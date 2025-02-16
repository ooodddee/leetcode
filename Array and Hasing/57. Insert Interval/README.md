## 57. Insert Interval
<https://leetcode.com/problems/insert-interval/>


=======================================================================================<br>

### UMPIRE Method:
#### Understand


1. empty?
    * no
2. sorted:
    * no
    

### Match

1. sorting


### Plan
1. Sort the intervals by the start value.
2. Initialize a result list with the first interval.
3. Iterate through the sorted intervals:
    1. If the current interval overlaps with the last interval in the result, merge them.
    2. Otherwise, add the interval as a new non-overlapping interval.
4. Return the result list.

### Implement

see solution.py

### Review

### Evaluate

- Time Complexity: O(nlog n), sorting: O(nlog n), iterating : O(n),
    
- Space Complexity: O(N)
    