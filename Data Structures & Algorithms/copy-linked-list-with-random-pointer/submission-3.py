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
        new  = {None:None}
        curr = head

        while curr:
            new[curr] = Node(curr.val)
            curr = curr.next
        
        copy = Node(0)

        copy_curr = copy
        curr = head
        while curr:
            copy_curr.next = new[curr]
            copy_curr.next.random = new[curr.random]
            copy_curr.next.next = new[curr.next]
            curr = curr.next
            copy_curr = copy_curr.next

        return copy.next