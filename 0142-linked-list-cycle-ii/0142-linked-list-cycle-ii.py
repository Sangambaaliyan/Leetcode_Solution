# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        i=0
        s= head
        f=head
        while f!=None and f.next!=None:
            s=s.next
            
            f=f.next.next
            if s==f:
                i+=1
                break
        if i>0:
            j=0
            f=f.next
            while f!=s:
                f=f.next
                j+=1
            j+=1
        else:
            return None

        s=head
        f=head
        for i in range(j):
            f=f.next
        while s!=f:
            f=f.next
            s=s.next
        return s
