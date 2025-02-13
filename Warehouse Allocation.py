from typing import List

class Solution:
    def findMinimumOperations(self, boxes: List[int]) -> int:
        n = len(boxes)
        total = sum(boxes)
        mean = total // n  # Average number of boxes
        r = total % n  # Remainder, tells how many piles need one more box
        
        excess = 0  # Total excess of boxes
        countAbove = 0  # Count of piles with more than the average boxes
        
        for b in boxes:
            if b > mean:
                excess += b - mean
                countAbove += 1
        
        return excess - min(r, countAbove)

solution = Solution()
boxes = [4, 4, 4, 4]
print(solution.findMinimumOperations(boxes))