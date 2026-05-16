# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen_nums = set()
        if head is None:
            return False
        while head.next != None:
            if head.val in seen_nums:
                return True
            seen_nums.add(head.val)
            head = head.next
        
        return False