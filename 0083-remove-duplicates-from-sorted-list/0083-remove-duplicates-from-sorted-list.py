# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current:
            # does the next node exist and is the value of it equal to the head node?
            while current.next and current.next.val == current.val:
                #if it is then the next node is the nextnext
                current.next = current.next.next
            #move current to the next node since that req is met or isnt met to iterate thru the entire linked list 
            current = current.next
        return head
                