class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        stack=[]
        s=sorted(s)
        l=0
        stack=[s[0]]
        for i in range(1,len(s)):
            if len(stack)!=0 and stack[-1]==s[i]:
                stack.pop()
                l+=2
            else:
                stack.append(s[i])
        if len(stack)==0:
            pass
        else:
            l+=1
        return l
            
        