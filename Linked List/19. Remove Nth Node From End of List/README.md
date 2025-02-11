## 19. Remove Nth Node From End of List
<https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/>


=======================================================================================<br>

### UMPIRE Method:
#### Understand


1. empty?
    * no, the list has at least 1 node
2. edge case:
    * What if both lists are empty? Return None
    * What if one list is empty? Return the non-empty list
3. edge case:
    * even length: 1 -> 2 -> 3 -> , 1 → 4 → 2 → 3
    * odd length: 1 → 2 → 3 → 4 → 5,  1 → 5 → 2 → 4 → 3
    * Single node: 1, 1 (no change)
    * two nodes: 1 -> 2, 1 -> 2 (no change)


### Match

1. Two Pointers: Finding the middle of the list.
2. Reversing a Linked List: reorder the second half.
3. Merging Two Linked Lists: Combining the two halves in alternating order.

### Plan
1. Fast and slow pointers to find the middle node
2. Reverse the list from the middle to the end (need to break the two parts of the Linked List)
3. Use while loop to merge (while h2):
    1. h1 = head, h2 = pre, t1 = h1.next, t2 = h2.next
    2. h1.next = h2, h2.next = t1
    3. h1, h2 = t1, t2

### Implement

see solution.py

### Review

### Evaluate




- Time Complexity: O(N), (Traverses the list three times)
    
- Space Complexity: O(1), (No extra data structures used)
    