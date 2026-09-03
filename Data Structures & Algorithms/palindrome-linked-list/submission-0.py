# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        f, s = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
        mid = s
        p = mid
        prev = None
        while mid:
            next = mid.next
            mid.next = prev
            prev = mid
            mid = next
        s = prev
        while s:
            if head.val != s.val:
                return False
            s = s.next
            head = head.next
            
        return True
