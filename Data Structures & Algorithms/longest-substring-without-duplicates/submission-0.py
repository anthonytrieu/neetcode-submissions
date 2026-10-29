class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # hash set for unique values
        charSet = set()
        left = 0
        length = 0

        # right pointer will always be moving to the right
        for right in range(len(s)):
            # if we get a duplicate character we need to move left pointer one over and remove from the char from the set
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            # add right element to charset and update the max length
            charSet.add(s[right])
            length = max(length, right - left + 1) # + 1 because inclusivity 

        return length