class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # going to sort each string, but we need to make
        # a defaultdic that maps the sorted string to its
        # original rearrangement

        res = defaultdict(list)

        for s in strs:
            # sort and join the words
            sortedS = ''.join(sorted(s))

            # append the original word to bucket (res)
            res[sortedS].append(s)
        return list(res.values())