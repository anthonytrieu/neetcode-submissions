class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # make a hash set
        hashset = set()
        # append to the hash set if not seen
        for i in range(len(nums)):
            if nums[i] not in hashset:
                hashset.add(nums[i])
        # return True if value appears more than once
            else:
                return True
        # return False if values do not appear more than once
        return False