# Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        k = 1  
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]  
                k += 1

        for j in range(k, len(nums)):
            nums[j] = "_"       # type: ignore

        return k

nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
k = sol.removeDuplicates(nums)

print("k =", k)      
print("nums =", nums) # nums = [0,1,2,3,4,'_','_','_','_','_']
