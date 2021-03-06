# Given a linked list, reverse the nodes of a linked list k at a time and return
#  its modified list. 
# 
#  k is a positive integer and is less than or equal to the length of the linked
#  list. If the number of nodes is not a multiple of k then left-out nodes in the 
# end should remain as it is. 
# 
#  
#  
# 
#  Example: 
# 
#  Given this linked list: 1->2->3->4->5 
# 
#  For k = 2, you should return: 2->1->4->3->5 
# 
#  For k = 3, you should return: 3->2->1->4->5 
# 
#  Note: 
# 
#  
#  Only constant extra memory is allowed. 
#  You may not alter the values in the list's nodes, only nodes itself may be ch
# anged. 
#  
#  Related Topics 链表 
#  👍 638 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            pre.next = head
            tail.next = nex
            pre = tail
            head = pre.next

        return dummy.next

    def reverse(self, head, tail):
        pre = tail.next
        cur = head
        while pre != tail:
            cur.next, cur, pre = pre, cur.next, cur
        return tail, head

# leetcode submit region end(Prohibit modification and deletion)
