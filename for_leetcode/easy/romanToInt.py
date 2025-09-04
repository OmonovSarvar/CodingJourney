class Solution:
    def romanToInt(self, s: str) -> int:
        mapping={
                "I": 1, 
                "V": 5, 
                "X": 10, 
                "L": 50, 
                "C": 100, 
                "D": 500, 
                "M": 1000
                }
        total=0
        for i in range(len(s)-1):
            if mapping[s[i]]<mapping[s[i+1]]:
                total-=mapping[s[i]]
            else:
                total+=mapping[s[i]]
        total+=mapping[s[-1]]
        return total
    
    
sol = Solution()
print(sol.romanToInt("III")) # 3
print(sol.romanToInt("LVIII")) # 58
print(sol.romanToInt("MMVII")) # 2007