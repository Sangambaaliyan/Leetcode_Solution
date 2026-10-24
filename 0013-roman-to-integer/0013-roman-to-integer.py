class Solution:
    def romanToInt(self, s: str) -> int:
        h={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        d=0
        i=0
        while(i<len(s)):
            if (i+1) < len(s) and h[s[i]]<h[s[i+1]]:
                sub=h[s[i+1]]-h[s[i]]
                d+=sub
                i+=2
            else:
                d+=h[s[i]]
                i+=1
        return d
        