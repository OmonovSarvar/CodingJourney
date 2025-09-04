class Solution:
    def isPalindrome(self, x: int)-> bool:
        if x<0:
            return False
        return str(x)==str(x)[::-1]

sol = Solution()

print(sol.isPalindrome(121)) # True
print(sol.isPalindrome(-121)) # False 
print(sol.isPalindrome(10)) # False
