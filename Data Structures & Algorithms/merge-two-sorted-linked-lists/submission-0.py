# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node
        dummy = ListNode(0)
        curr = dummy


        # compare list1 with list2 by size of element 

        while list1 and list2:
            if list1.val < list2.val: # list1 linked list
                # connect smaller node to dummy node
                curr.next = list1
                # move current forward
                curr = curr.next
                # move l1 forward
                list1 = list1.next

            else: # list2 linked list
                curr.next = list2
                curr = curr.next
                list2 = list2.next
        
        # attach the remaining nodes
        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return dummy.next
















    # # brute force: connect the two lists together. Change into array -> sort it afterwards -> back to linked list
    #     def combineList(list1,list2):
    #         # empty list
    #         if not list1:
    #             return list2
    #         # traverse to last node of list 1
    #         curr = list1
    #         while curr.next:
    #             curr = curr.next
    #         # point the last node of list 1 to list 2
    #         curr.next = list2
    #         return list1

    #     # combine the linked lists    
    #     head = combineList(list1,list2)
    #     # change linked list to an array 
    #     values = []
    #     curr = head
    #     while curr:
    #         values.append(curr.val)
    #         curr = curr.next
    #     # sort the array
    #     values.sort()

    #     # change array back to linked list
    #     dummy = ListNode(0)
    #     curr = dummy

    #     for value in values:
    #         curr.next = ListNode(value) # sets up access to the next node
    #         curr = curr.next # moves our current variable to the next node
    #     return dummy.next





