class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hash_set = set()
        max_counter = 0

        l = 0
        
        for r in range(len(s)):
            while s[r] in hash_set:
                hash_set.discard(s[l])
                l += 1
            hash_set.add(s[r])
            max_counter = max(max_counter,r - l + 1)

        return max_counter








        # for i in range(len(s)):
        #     if s[i] not in hash_set:
        #         hash_set.add(s[i])
        #         r += 1
        #         curr_counter = r - l + 1
        #     else:
        #         hash_set.discard(s[l])
        #         l += 1
        #         max_counter = max(curr_counter,max_counter)
        # return max_counter

            
            





        # we will be using a hashset to set this up. Append everytime to #hash map if there is a new character. Increment counter as well. If #there is a new character, we stop and return the counter.