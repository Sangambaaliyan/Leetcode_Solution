# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        l=0
        le=head
        if not head:
            return None
        while le.next:
            le=le.next
            l+=1
        l+=1
        k=k%l
        current=head
        for i in range(l-k-1):
            current=current.next
        le.next=head
        head=current.next
        current.next=None
        return head
        