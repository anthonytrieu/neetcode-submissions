class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute force: sort both arrays and compare them

        # initialize array
        a = []
        b = []

        # append array s to a
        for i in s:
            a.append(i)
        a.sort()
        for i in t:
            b.append(i)
        b.sort()
        return a == b
             


            
