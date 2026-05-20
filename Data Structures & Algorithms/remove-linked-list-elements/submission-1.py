# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 2 -> 1 -> 4 -> None
        '''
        There are 3 options we are in the middle of two other nodes
        We are the beginning or we are at the end 
        '''
        start = ListNode(0)
        start.next = head
        prev = start
        curr = head 
        while curr is not None:
            if curr.val == val:
                prev.next = curr.next 
                curr = prev
            else:
                prev = curr
                curr = curr.next
        return start.next


