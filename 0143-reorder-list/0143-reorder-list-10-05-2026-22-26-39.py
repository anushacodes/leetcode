# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # two pointers
        # first, last -> head and tail(how tail??)
        # tail inserted btw 
        # first = head
        # # traverse to end to find tail? 
            # can't reverse tail!!
            # need to take last n elems and store somehwere?
            # can i reverse half ll?
            # how to find mid? ans: fast and slow pointers
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow

        # split and reverse from slow
        prev, curr = None, slow.next
        slow.next = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first = head
        sec = prev

        while sec:
            # merge 2 ll
            temp = first.next
            temp2 = sec.next

            first.next = sec
            sec.next = temp

            first = temp
            sec = temp2


        

        







        