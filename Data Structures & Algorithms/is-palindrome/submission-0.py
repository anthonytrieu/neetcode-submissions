class Solution:
    def isPalindrome(self, s: str) -> bool:

        # remove all space, lowercase the string, and puncutation
        newString = s.replace(" ","").lower()
        newStr = ""
        for c in newString:
            if c.isalnum():
                newStr += c 
        left = 0
        right = len(newStr) - 1
        
        while left < right:
            if newStr[left] == newStr[right]:
                left = left + 1
                right = right - 1

            else:
                return False
        return True
            
            
