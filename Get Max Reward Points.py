from typing import List

class Solution:
  def getMaxRewardPoints(self, reward: List[int]) -> int:
    reward.sort(reverse = True)
    n = len(reward)
    res = 0
      
    for i in range(n):
        res += reward[i]
        for j in range(i + 1, n):
            if reward[j] > 0:
                reward[j] = reward[j] - 1
    
    return res