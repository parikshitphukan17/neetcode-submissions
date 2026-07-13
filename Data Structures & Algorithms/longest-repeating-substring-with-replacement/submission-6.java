class Solution {
    public int characterReplacement(String s, int k) {
        int l,maxCnt=0;
        l=0;
        Map<Character,Integer> cnt = new HashMap<>();
        int res = 0;
        for(int r = 0; r<s.length();r++){
            var c = s.charAt(r);
            cnt.put(c,cnt.getOrDefault(c,0)+1);
            maxCnt = Math.max(maxCnt,cnt.get(c));
            while(r-l+1-maxCnt>k){
                cnt.put(s.charAt(l),cnt.get(s.charAt(l))-1);
                l+=1;

            }
            res = Math.max(res,r-l+1);

            
        }
        return res;
        //     1   2   3   4   5   6   7   8
        // r   r   r   r   r   r   r   r   r
        // l   l   l   l
        // A   A   A   B   A   B   B   B   B

        // 5-4 = 1

        // while r-l+1-maxF>k{
        //     l+=1


        // }
        
    }
}
