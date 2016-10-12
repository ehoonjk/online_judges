# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = head
        even = even_head = head.next
        node = head
        count = 1
        
        while node:
            odd.next = node.next.next
            even.next = node.next
            node = node.next.next
        while True:
            if count % 2 == 0: # when even
                temp = even.next.next
                even.next = even.next.next
                even = temp
            else:
                temp = odd.next.next
                odd.next = odd.next.next
                odd = temp
            if not node.next:
                odd.next = even_head
                break
            count+=1
            
        return head