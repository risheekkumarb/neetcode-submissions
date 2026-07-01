from heapq import heapify, heappop, heappush

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = [(o.val, i, o) for i,o in enumerate(lists)]
        heapify(min_heap)

        dummy = ListNode(0)
        curr  = dummy
        while min_heap:
            num, i, ll = heappop(min_heap)
            curr.next = ListNode(num)
            curr = curr.next
            if ll.next: heappush(min_heap, (ll.next.val, i, ll.next))
        
        return dummy.next