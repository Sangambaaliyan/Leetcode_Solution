class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack1=[]
        stack2=[]
        for i in s:
            if i=="#":
                if len(stack1)!=0:
                     stack1.pop()
                else:
                    continue
            else:
                stack1.append(i)
        for i in t:
            if i=="#":
                if len(stack2)!=0:
                     stack2.pop()
                else:
                    continue
            else:
                stack2.append(i)
        if len(stack1)!=len(stack2):
            return False
        else:
            while len(stack1)!=0:
                if stack1.pop()==stack2.pop():
                    continue
                else:
                    return False
            return True