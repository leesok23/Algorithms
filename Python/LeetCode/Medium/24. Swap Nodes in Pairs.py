# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        p1 = head
        while p1 and p1.next:
            p1.val, p1.next.val = p1.next.val, p1.val
            p1 = p1.next.next
            if not p1 or not p1.next:
                return head
        return head
