# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        root = ListNode(-1)
        I = root
        while True:
            if l1.val < l2.val:
                I.next = ListNode(l1.val)
                l1 = l1.next
                if l1 == None:
                    I.next.next = l2
                    return root.next
            else:
                I.next = ListNode(l2.val)
                l2 = l2.next
                if l2 == None:
                    I.next.next = l1
                    return root.next
            I = I.next
