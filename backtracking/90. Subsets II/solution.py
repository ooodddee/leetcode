# Set
def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        path = []

        def dfs(i):
            if i == len(nums):
                res.add(tuple(path.copy())) #
                return
            
            path.append(nums[i])
            dfs(i + 1)
        
            path.pop()
            dfs(i + 1)
        
        dfs(0)
        return list(res) #

# Sorting + Pruning Duplicates
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        nums.sort()

        def dfs(i):
            if i == len(nums):
                res.append(path.copy())
                return

            # Include current element
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

            # Skip duplicate elements
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1 # Move index forward to skip duplicate numbers
            
            # Exclude current element and move forward
            dfs(i + 1)

        dfs(0)
        return res
