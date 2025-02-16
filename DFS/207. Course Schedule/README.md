## 207. Course Schedule
<https://leetcode.com/problems/course-schedule/description/>


=======================================================================================<br>

### UMPIRE Method:
#### Understand


1. What if there are no prerequisites?
    * return True
2. Are there self-loops (like [0,0])?
    * No, ai ≠ bi always.
3. edge case:
    * No prerequisites : prerequisites = [] : True
    * Single valid dependency : prerequisites = [[1, 0]] : True
    * Cycle exists : [[0,1],[1,0]] : False
    * Disconnected courses : prerequisites = [[1,0],[3,2]] : True


### Match

detecting cycles in a directed graph. If a cycle exists, it means we cannot complete all courses.
1. DFS (recursion)
2. BFS (topological sorting / Kahn's algorithm)


### Plan
1. bulid an adjacency list:
    * adj[a] = [b1, b2, ...] a depends on b1, b2, ...
    * store visited nodes in vis (set) to track cycle
2. dfs function:
    * a course is alreadly visited -> return False
    * a course has no prerequisites -> return True
    * recursively check: if any prerequisite cannot be complete(False) -> return False
    * backtrack (remove from vis set) once we finish exploring
    * mark course as completed (adj[cur] = [])
3. try every course


### Implement

see solution.py

### Review

### Evaluate

E is the number of prerequisite pairs.
V is the number of numCourses


- Time Complexity: O(V + E), 
    
- Space Complexity: O(V + E),  
    