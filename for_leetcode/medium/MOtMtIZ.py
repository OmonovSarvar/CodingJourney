# Minium Operators to Make the Integer Zero
# https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/description/
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int: #type:ignore
        if num1 == 0:
            return 0
        elif num1 < 0:
            return -1
        for i in range(1, 33):
            target = num1 - i * num2
            if num1 < 0:
                return -1
            elif bin(num1).count('1') <= i <= num1:
                return i
        
sol = Solution()
print(sol.makeTheIntegerZero(3, -2))
print(sol.makeTheIntegerZero(5, 7))
        
        
        
        
        
        
        
        
        
        
        
        
        