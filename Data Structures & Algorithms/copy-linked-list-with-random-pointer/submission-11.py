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
        old2new = {None:None}
        curr = head
        while curr:
            node = Node(curr.val)
            old2new[curr] = node
            curr = curr.next
        
        curr = head
        while curr:
            old2new[curr].next = old2new[curr.next]
            old2new[curr].random = old2new[curr.random]
            curr = curr.next
        return old2new[head]