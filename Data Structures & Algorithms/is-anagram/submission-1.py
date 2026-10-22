class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       # len check
        if len(s) != len(t):
            return False
       # sort it then compare it
        a = sorted(s)
        b = sorted(t)
        return a == b