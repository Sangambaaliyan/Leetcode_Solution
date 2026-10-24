import itertools
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        h={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        s=[]
        if not digits:
            return []
        for i in digits:
            s.append(h[i])
        result=itertools.product(*s)
        n=list("".join(p) for p in result)
        return n


        