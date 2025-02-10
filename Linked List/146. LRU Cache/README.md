## 146. LRU Cache
<https://leetcode.com/problems/lru-cache/>


=======================================================================================<br>

### UMPIRE Method:
#### Understand


1. Any requirement on time/space complexity?

2. Can the input be empty?
    * no, `nums.length` is at least 1.
3. Are there duplicate elements in the input?
    * yes, the result must not contain duplicate subsets
4. ***sorted?***
    * no
4. What is the range of the size of the input array nums? Is there a maximum number of elements that nums can have?


### Match

1. set:
    * initialize an empty set `res` to store the result, initialize an empty array  `path` to store the subsets

2. Sorting + Pruning Duplicates
    * Sort the input array nums to group duplicates together.
    * pruning: If the current element is the same as the previous element, skip it to avoid generating duplicate subsets.
    


### Plan
1. Initialize an empty array `res` to store the result, Initialize an empty array  `path` to store the subsets
2. Sort the input array nums to group duplicates together.
3. define a recursion function dfs(i):
    * edge case: if i == lenght of nums
        * add a copyt of path to res
        * break the dfs
    * recursion case:
    * include nums[i]:
        * add nums[i] to the path
        * call dfs(i + 1)
    * Skip duplicate elements using a while loop
        * Ensures that we do not go out of bounds
        * If the current element nums[i] is equal to the next element nums[i + 1], it means it's a duplicate.
    * exclude nums[i]:
        * remove the last element from path (backtrack)
        * call dfs(i + 1)
3. call dfs(0) to start backtracking
4. return res



### Implement

see solution.py

### Review

### Evaluate


Assume `N` is the length of the input string

- Time Complexity: O(N * 2^N)
    * O(2^N) * O(N)  (number of call) * (copying subset)
- Space Complexity: O(N * 2^N)
    * recursion stack: O(N) depth, O(N) space usage
    * storage for subsets: O(2^N) subsets, each having a maximum lenght of n, O(N * 2^N)