# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = head
        fast = head

        while fast and fast.next:
            # fast and slow pointers will eventually meet if cycle
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False





        #how can we compare the node objects to see when they meet up




        # For this implementation, we don't need curr_node = head. Just used for my understanding
        
        # visited = set()

        # while head:  
        #     curr_node = head
        #     if curr_node in visited:
        #         return True              
        #     visited.add(curr_node)
        #     head = head.next
        # return False

        # time complexity: o(n) we need to loop through the whole list
        # space complexity: o(n) need to store the linked list in its entirity 




        