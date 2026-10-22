class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # double for loop to compare all numbers
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
        return False

# how to skip comparing element by itself
# trace the code and see what is happening