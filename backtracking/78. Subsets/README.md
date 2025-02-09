## 78. Subsets
<https://leetcode.com/problems/subsets/>


=======================================================================================<br>

### UMPIRE Method:
#### Understand


1. Any requirement on time/space complexity?

2. Can the input be empty?
    * no, `nums.length` is at least 1.
3. Are there duplicate elements in the input?
    * No, all elements are unique.
4. What is the range of the size of the input array nums? Is there a maximum number of elements that nums can have?


### Match


backtracking
1. Use Backtracking (DFS) to explore all possible subsets.
2. Maintain a temporary list path to store the current subset.
3. At each step, make a decision:
    * Include the current element and recurse.
    * Exclude the current element and recurse.
4. Once we reach the end of the array, store the subset.
    


### Plan
1. Initialize an empty array `res` to store the result, Initialize an empty array  `path` to store the subsets
2. define a `dfs` function to backtrack, starting with index i = 0:
    * edge case: if i == lenght of nums
        * add a copyt of path to res
        * break the dfs
    * include nums[i]:
        * add nums[i] to the path
        * call dfs(i + 1)
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
    * The total number of nodes in the recursion tree is 2^n, because each element has two choices (to be included or not). 
    * Each node requires O(N)  time to copy the path, so the overall time complexity is O(N * 2^n). 
- Space Complexity: O(N * 2^N)
    * For the total space of the recursion call stack, it is O(N)
    * For the space complexity of storing the result res:
        *The total number of subsets is 2^n, 
        * The average length of each subset is n/2, 
        * Therefore, the total space required to store all subsets is O(n/2 * 2^n), which simplifies to O(N * 2^n)