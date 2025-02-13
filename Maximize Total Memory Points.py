class Solution:
  def maximizeTotalMemoryPoints(self, memory):
    # Sort the memory values in descending order to maximize cumulative sums
    memory.sort(reverse=True)
    
    # Compute prefix sums to accumulate memory points
    for i in range(1, len(memory)):
        memory[i] += memory[i - 1]  # Add the previous chapter's memory points
    
    # Return the total sum of accumulated memory points
    return sum(memory)

memory = [3, 4, 5]
solution = Solution()
print(solution.maximizeTotalMemoryPoints(memory))