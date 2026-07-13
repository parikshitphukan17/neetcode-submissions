class Solution {
    public List<Integer> partitionLabels(String s) {
        int l=0,r=0,last = 0;
        Map<Character,Integer> map = new HashMap<>();
        for(int i=0;i<s.length();i++){
            Character c = s.charAt(i);
            map.put(c,i);
        }
        List<Integer> res = new ArrayList<>();
        
        while(r<s.length()){
            last = Math.max(map.get(s.charAt(l)),last);
            while(r<=last){
                last = Math.max(map.get(s.charAt(r)),last);
                r++;
            }
            res.add(r-l);
            l=r;
        }
        return res;
        

        // l,r,last = 0
        // res = 0;
        // while r<s.length
        //     res++;
        
                        
        // l,r         r   r
        // x   y   x   x   y   z   b   z   b   b   i   s
        
    }
}
