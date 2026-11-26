"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # walk through once to copy list
        # walk through second time to copy the random pointers
        # hash map needed to store random index data
        hs = {None:None} # need to associate something with additional information

        if head is None:
            return head

        
        current = head
        # one pass
        while current:
            new_node = Node(current.val) # Create a new node
            hs[current] = new_node # original linked list matches with new linked list
            current = current.next
        
        # second pass
        current = head

        while current:
            new_node = hs[current]
            hs[current].next = hs[current.next]
            new_node.random = hs[current.random]
            current = current.next
        return hs[head]

            

        
            








        