# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        maxPair = 0
        s,f = head, head
        while f and f.next:
            f = f.next.next
            s = s.next
        mid = s
        prev = None
        while mid:
            n = mid.next
            mid.next = prev
            prev = mid
            mid = n
        mid = prev
        s = head
        while mid:
            maxPair = max(maxPair, mid.val + s.val)
            mid = mid.next
            s = s.next
        return maxPair