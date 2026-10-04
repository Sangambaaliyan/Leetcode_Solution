class Solution(object):
    def nextGreaterElements(self, nums2):
        """
        :type nums2: List[int]
        :rtype: List[int]
        """
        st = []
        leg = len(nums2)
        arr = [0] * leg
        
       
        for i in range(2 * leg - 1, -1, -1):
            idx = i % leg 
            
            if len(st) == 0:
                st.append(nums2[idx])
                if i < leg:
                    arr[idx] = -1
            else:
                if nums2[idx] < st[-1]:
                    if i < leg:
                        arr[idx] = st[-1]
                    st.append(nums2[idx])
                else:
                    while len(st) != 0 and nums2[idx] >= st[-1]: 
                        st.pop()
                    if len(st) == 0:
                        if i < leg:
                            arr[idx] = -1
                    else:
                        if i < leg:
                            arr[idx] = st[-1]
                    st.append(nums2[idx])
                    
        return arr
