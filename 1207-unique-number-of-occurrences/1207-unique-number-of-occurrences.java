class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        HashMap<Integer,Integer> h =new HashMap<>();
         int l= arr.length;
        for(int i=0;i<l;i++){
            if(h.containsKey(arr[i])){
                h.put(arr[i], h.getOrDefault(arr[i], 0) + 1);
            }
            else{
                h.put(arr[i],1);
            }

        }
        Integer[] a = h.values().toArray(new Integer[0]);
        Set<Integer> s =new HashSet<>(Arrays.asList(a));
        return a.length==s.size();
        
    }
}