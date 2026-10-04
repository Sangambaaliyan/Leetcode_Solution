class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        h={ ')': '(', '}': '{', ']':'['}
        stack1=[]
        leng =len(s)
        for i in range(leng):
            if len(stack1)!=0 :
                if s[i] in h.keys():
                    if h[s[i]] == stack1[-1]:
                        stack1.pop()
                    else:
                        return False
                else:
                    stack1.append(s[i])
                    
            else:
                    stack1.append(s[i])
        return len(stack1)==0