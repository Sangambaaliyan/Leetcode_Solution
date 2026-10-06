# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Queue:
    def __init__(self):
        self.q=[]
        self.front=-1
    def push(self,x):
        if self.front==-1:
            self.q.append(x)
            self.front+=1
        else:
             self.q.append(x)
    def pop(self):
        if len(self.q)==0:
            return -1
        x= self.q[self.front]
        self.front+=1
        if self.front==len(self.q):
             self.front=-1
             self.q=[]
        return x
    def getfront(self):
        if len(self.q==0):
            return -1
        return self.q[self.front]
    def size(self):
        if len(self.q)==0:
            return 0
        return len(self.q)-self.front
class Solution(object):

    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        q = Queue()
        ans=[]
        if root is None:
            return []
        q.push(root)
        ans.append(root.val)
        while q.size()>0:
            l=0
            j=0
            for i in range(q.size()):
                front=q.pop()
                if front.left!=None:
                    q.push(front.left)
                    l+=front.left.val
                    j+=1
                if front.right!=None:
                    q.push(front.right)
                    l+=front.right.val
                    j+=1
            if j!=0:
                 a=float(l)/j
                 ans.append(a)
        return ans
                
        