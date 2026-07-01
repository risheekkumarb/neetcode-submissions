class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self): return f'(value={self.val}, next={self.next})'

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        secondHalf = slow.next
        secondHalfrev, slow.next = None, None
        
        while secondHalf:
            temp = secondHalf.next
            secondHalf.next = secondHalfrev
            secondHalfrev = secondHalf
            secondHalf = temp
        # print(head, secondHalfrev)
        curr = head
        while secondHalfrev:
            temp = curr.next
            curr.next = secondHalfrev
            secondHalfrev = secondHalfrev.next
            curr.next.next = temp
            curr = temp
        # print(head)
        # return head