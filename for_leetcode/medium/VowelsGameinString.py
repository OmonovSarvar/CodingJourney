# Vowels Game in String
# https://leetcode.com/problems/vowels-game-in-a-string/description/

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(ch in "aeiou" for ch in s.lower())

            
sol = Solution()
print(sol.doesAliceWin("leetcoder")) # true
print(sol.doesAliceWin("bc")) # false
