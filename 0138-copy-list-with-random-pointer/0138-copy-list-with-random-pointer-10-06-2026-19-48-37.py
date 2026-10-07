"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        copy = dummy
        curr = head
        pdict = {None:None} 

        while curr:
            # creating new ll w no random, saved old->new pointer in dict
            new = Node(curr.val)
            copy.next = new
            pdict[curr] = new
            copy = new
            curr = curr.next

        curr = head
        copy = dummy.next

        while curr:
            # find copy of org random
            copy.random = pdict[curr.random]
            copy = copy.next
            curr = curr.next

        return dummy.next



