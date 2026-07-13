class Solution {
    public int lengthOfLongestSubstring(String s) {
        // l   l       r
        // z   x   y   z   x   y   z           {z:0 , x:1 , y:2}

        // check if val in hasmap yes then change l point to max of current or val+1

        int l,r,res;
        Map<Character,Integer> map = new HashMap<>();
        l=0;
        r=0;
        res = 0;
        while(r<s.length()){
            var val = s.charAt(r);
            if(map.containsKey(val)){
                l = Math.max(l,map.get(val)+1);
            }
            map.put(val,r);
            res = Math.max(res,r-l+1);
            r++;
        }
        return res;
        

        
    }
}
