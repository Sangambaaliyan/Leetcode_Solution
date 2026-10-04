class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        st=[]
        leg = len(nums2)
        arr={}
        for i in range(leg-1,-1,-1):
            if len(st)==0:
                st.append(nums2[i])
                arr[nums2[i]]=-1
            else:
                if nums2[i]<st[-1]:
                    arr[nums2[i]]=st[-1]
                    st.append(nums2[i])
                else:
                    while len(st)!=0 and nums2[i]>st[-1] :
                        st.pop()
                    if len(st)==0:
                        arr[nums2[i]]=-1
                    else:
                        arr[nums2[i]]=st[-1]
                    st.append(nums2[i])
        res=[]
        for i in nums1:
            res.append(arr[i])
        return res