# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        a= head
        p=None
        n=None
        while a!=None:
            n=a.next
            a.next=p
            p=a
            a=n
        head= p
        return head