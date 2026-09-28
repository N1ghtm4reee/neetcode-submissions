# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # fast slow pointer 
        f = head
        s = head
        while f and f.next:
            s = s.next
            f = f.next.next
        # p will be in the middle node
        # reverse the second half
        curr = s
        prev = None
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        f = head
        s = prev
        while s:
            # check if equal
            if s.val != f.val:
                return False
            s = s.next
            f = f.next
        return True