

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        ptr = head
        tmp = 0
        while True:
            s = 0
            if l1 != None:
                s = s + l1.val
                l1 = l1.next
            if l2 != None:
                s = s + l2.val
                l2 = l2.next
            s = s + tmp
            if s >= 10:
                ptr.val = s - 10
                tmp = 1
            else:
                ptr.val = s
                tmp = 0
            if (l1 == None) and (l2 == None) and (tmp == 0):  # terminate the loop in the end
                return head
            ptr.next = ListNode(0)
            ptr = ptr.next
