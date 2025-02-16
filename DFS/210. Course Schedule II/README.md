## 210. Course Schedule II
<https://leetcode.com/problems/course-schedule-ii/description/s>


=======================================================================================<br>

### UMPIRE Method:
#### Understand


1. empty?
    * no, the list has at least 1 node
2. edge case:
    * only one node, remove first
    * remove head node
    * remove last node
3. what if n is invalid? (greater than length of list)
    * n is always valid



### Match

1. fast and slow pointers
2. dummy node (to handle edge cases (removing the head))


### Plan
1. use dummy node pointing to head, both fast and slow start at dummy
2. move fast pointer n steps forward
3. move fast and slow together, when fast reaches the end, slow is right before the node to remove
4. change slow.next to slow.next.next

### Implement

see solution.py

### Review

### Evaluate




- Time Complexity: O(N), 
    
- Space Complexity: O(1), (No extra data structures used)
    