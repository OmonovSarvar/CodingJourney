# 1317. Convert Integer to the Sum of Two No-Zero Integers
# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]: #type: ignore
        for i in range(1, n):
            a, b = i, n - i
            if '0' not in str(a) and '0' not in str(b):
                return [a, b]
        
        
sol = Solution()
print(sol.getNoZeroIntegers(11))