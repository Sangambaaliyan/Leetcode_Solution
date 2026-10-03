class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
            
        pointerA = headA
        pointerB = headB
        
        while pointerA is not pointerB:
            pointerA = headB if pointerA is None else pointerA.next
            pointerB = headA if pointerB is None else pointerB.next
            
        return pointerA
