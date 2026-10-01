# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            csum = v1 + v2 + carry
            curr.next = ListNode(csum%10)
            carry = csum // 10
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry: curr.next = ListNode(carry)
        return dummy.next