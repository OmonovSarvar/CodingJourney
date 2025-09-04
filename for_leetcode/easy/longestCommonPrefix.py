class Solution:
    def longestCommonPrefix(self, strs: list[str])-> str:
        if not strs:
            return ""

        prefix = ""
        first_word = strs[0]

        for i in range(len(first_word)):
            char = first_word[i]

            # Boshqa hamma so'zlarda shu harf mosligini tekshiramiz
            for word in strs[1:]:
                if i >= len(word) or word[i] != char:
                    return prefix  # shu joyda moslik buziladi
            
            prefix += char  # agar mos bo‘lsa, qo‘shib qo‘yiladi
        
        return prefix
    
sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"])) # "fl"
print(sol.longestCommonPrefix(["dog","racecar","car"]))     # ""
print(sol.longestCommonPrefix(["apple","app","application"])) # "app"