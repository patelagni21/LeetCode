# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        #if head isnt non existant
        while head:
            # cause it cant repeat so if it does it must be True that its a cycle
            if head in nodes:
                return True
            #if not we add to our hashset and make our pointer to the next node
            nodes.add(head)
            head = head.next
        return False