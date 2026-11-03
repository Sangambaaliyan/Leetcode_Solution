class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        h={}
        l=[]
        for i in paths:
            l.append(i[0])
        for i in paths:
            if i[-1] in l:
                continue
            else:
                return i[-1]



        