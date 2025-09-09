# Number of People Aware of a Secret
# https://leetcode.com/problems/number-of-people-aware-of-a-secret/

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int: #type: ignore
        MOD = 10**9 + 7
        dp = [0] * n
        dp[0] = 1           

        active = 0           

        for day in range(1, n):
            if day - delay >= 0:
                active = (active + dp[day - delay]) % MOD

            if day - forget >= 0:
                active = (active - dp[day - forget]) % MOD

            dp[day] = active % MOD

        ans = sum(dp[max(0, n - forget): n]) % MOD
        return ans
    
    
sol = Solution()
print(sol.peopleAwareOfSecret(6, 2, 4))