# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        current = head
        while current is not None:    
            #holds
            next_node = current.next  # 1. Save the next node
            current.next = prev       # 2. Reverse the connection
            prev = current            # 3. Move prev forward
            current = next_node       # 4. Move current forward

        return prev



        