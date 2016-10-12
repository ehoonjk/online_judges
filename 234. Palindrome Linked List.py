# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        normal_node = head
        fast_node = head

        while fast_node.next and fast_node.next.next:
            fast_node = fast_node.next.next
            normal_node = normal_node.next

        prev_node, cur_node = normal_node, normal_node.next
        normal_node.next = None
        
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node

        fwd_node = head
        bwd_node = prev_node

        while fwd_node and bwd_node:
            if fwd_node.val != bwd_node.val:
                return False
            fwd_node = fwd_node.next
            bwd_node = bwd_node.next
        return True
