class Solution:
    def isValid(self, s: str) -> bool:
        # initialize stack
        stack = []

        # make the hash map
        match = { ")" : "(", "}" : "{", "]" : "[" }

        for character in s:
            if character in "[({":
                stack.append(character)
            else:
                if not stack:
                    return False
                # comparasion if it matches    
                # if the top of the stack matches character
                if stack[-1] != match.get(character):
                    return False
                stack.pop()
        return len(stack) == 0

# key takeaway
# hash map, append to stack and compare to stack, pop afterwards
# return true once stack is empty
        
            