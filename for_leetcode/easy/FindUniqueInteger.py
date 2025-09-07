# Find N Unique Integers Sum up to Zero
# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/


from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]: #type: ignore
        if n == 0:
            return []
        elif n % 2 == 0:
            half = n // 2
            return [i for i in range(-half, half + 1) if i != 0]
        elif n % 2 == 1:
            return [i for i in range(-(n // 2), (n // 2) + 1)]
    
sol = Solution()
print(sol.sumZero(5)) 
        
        
        
        