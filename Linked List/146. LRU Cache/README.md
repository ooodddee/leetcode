## 146. LRU Cache
<https://leetcode.com/problems/lru-cache/>


=======================================================================================<br>

### UMPIRE Method:
#### Understand


    1. Any requirement on time/space complexity?
        * The functions get and put must each run in O(1) average time complexity.


### Match

    1. HashMap: 
        1. Get: O(1), Put: O(1)
        2. Maps: key -> node
    2. Doubly Linked List:
        1. Remove: O(1), Insert: O(1)
        2. Head = most recently used, tail = least recently used
    


### Plan
        1. Class Node
            1. Key
            2. Value
            3. Pre
            4. Next
        2. Initialize LRU cache (self, capacity: int)
            1. Capacity
            2. Dummy node
            3. Dictionary 
        3. Function get (self, key: int)
            1. Node = get_node
            2. Return node.value if node else -1
        4. Function put (self, key: int, value: int)
            1. If node exist:
                1. Change value
            2. If not exist:
                1. Creat new node in dictionary
                2. Push_front
            3. If Out of capacity:
                1. Delete key at the map
                2. Remove the last node
        5. Function get_node (key)
            1. If not exist:
                1. Return None
            2. If  exist:
                1. Node = dic[key]
                2. remove(node)
                3. push_front(node)
        6. Function remove (key)
            1. Linked list
        7. Function push_front (key)
            1. Linked list






### Implement

see solution.py

### Review

### Evaluate


- Time Complexity: O(1)

- Space Complexity: O(N)
