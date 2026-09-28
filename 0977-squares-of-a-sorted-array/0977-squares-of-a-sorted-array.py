class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        a  = 0
        r= len(nums)-1
        pos =len(nums)-1
        re= [0]*(len(nums))
        while a<=r:
            if abs(nums[a])>abs(nums[r]):
                re[pos]=nums[a]**2
                pos-=1
                a+=1
            else:
                re[pos]=nums[r]**2
                pos-=1
                r-=1
        return re