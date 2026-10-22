from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash map and frequency counter of each int
        freq_map = defaultdict(int)
        
        for num in nums:
            freq_map[num] += 1 
        
        freq = [[] for i in range(len(nums) + 1)]
        # go through key value pair and append
        for key, value in freq_map.items():    
            freq[value].append(key)
        
        result = []
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

        return result


