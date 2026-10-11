# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        curr = head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy


        for _ in range (left - 1):
            prev = curr # 1
            curr = curr.next # 2 (left)
        
        tail = None # for rversing
        currtolast = curr   # save cur which will be last 
        prevtofirst = prev  # save to connect to first of reversed list

        # reverse from l to r
        # save prev and make last r point to next nodes
        for _ in range(right - left + 1): # 3 times
            temp = curr.next    # 3
            curr.next = tail    # 2->None
            tail = curr         # tail = 2 end = 3, 4
            curr = temp         # curr = 3 end = 4, 5

        prevtofirst.next = tail # 1-> 4
        currtolast.next = curr  # 2 -> 5

        return dummy.next
        