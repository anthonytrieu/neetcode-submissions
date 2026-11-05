# import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # indices of l,r,mid
        l = 0
        r = len(nums) - 1

        while (l <= r):
            # updates mid every iteration
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
            
            if target < nums[mid]:
                r = mid - 1

            if target > nums[mid]:
                l = mid + 1

        return -1

    # note:
    # we use l <= r instead of l<r because we may miss an element in the
    # array. It allows us to check every possible value before
    # giving up



















        # previous attempt, mid was not being updated. This will run n times regardless as well, so not optimal and not really binary search

        # mid = math.floor((l + r)/2)

        # for i in range(len(nums)):
        #     if target not in nums[i]:
        #         return -1
        #     if target == nums[mid]:
        #         return mid
            
        #     if target < nums[mid]:
        #         r = mid - 1
        #         mid = math.floor((l + r)/2)
            
        #     if target > nums[mid]:
        #         l = mid + 1
        #         mid = math.floor((l + r)/2)

        # return target

