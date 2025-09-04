class Solution:
    def findClosestPerson(self, x: int, y: int, z: int) -> int: #type: ignore
        distances = [abs(x-z), abs(y-z)]
        if distances[0] < distances[1]:
            return 1
        elif distances[0] > distances[1]:
            return 2
        elif distances[0] == distances[1]:
            return 0
        
        
sol = Solution()
print(sol.findClosestPerson(1, 2, 3)) # 2
print(sol.findClosestPerson(2, 1, 3)) # 1
print(sol.findClosestPerson(1, 1, 3)) # 0