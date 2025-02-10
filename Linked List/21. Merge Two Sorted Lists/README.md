## 21. Merge two sorted lists
<https://leetcode.com/problems/merge-two-sorted-lists/>


=======================================================================================<br>

### UMPIRE Method:
#### Understand


1. empty?
    * yes
2. edge case:
    * What if both lists are empty? Return None
    * What if one list is empty? Return the non-empty list
3. sorted?
    * yes
4. what if one of the lists is longer than the other? 
    * The longer list should be appended at the end once the shorter list is exhausted


### Match

1. Pointers: one for each list, and  compare the current nodes, append the smaller node to the new List

2. Dummy node:  simplify the logic of list merging, especially for handling edge cases, merged list is initially empty

### Plan
1. Create dummy node which head is None, and set a cur pointer to track the current node in the new list
2. Traverse both l1 and l2 simultaneously (While loop when l1 and l2):
    1. Same: put l1 to the new List, then move the l1 pointer
    2. Not same: put smaller one to the new list, then move the pointer of small one
    3. Move cur to cur.next after each insertion
3. After the loop, if there are any remaining nodes in either l1 or l2, attach them directly to cur.next
4. Return dummy.next (the head of new ListNode)

### Implement

see solution.py

### Review

### Evaluate




- Time Complexity: O(N + M)
    
- Space Complexity: O(1)
    