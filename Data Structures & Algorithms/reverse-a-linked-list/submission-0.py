# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Classic linked list problem need a 3 node solution

            0 ->      1    ->    2     ->    3
            curr     nxt        new
            past
        '''
        current = head 
        nxt = head
        past = None
        while(nxt != None): 
            new = nxt.next
            current = nxt
            current.next = past
            nxt = new
            past = current

        return current


            