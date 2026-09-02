# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        len = 0
        while fast and fast.next and fast.next:
            fast = fast.next.next
            len += 2
            slow = slow.next
        return slow