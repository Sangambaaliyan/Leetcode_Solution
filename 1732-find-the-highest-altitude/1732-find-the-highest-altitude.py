class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        m=0
        s=0
        for i in gain:
            s=s+i
            if s>m:
                m=s
        return m
        