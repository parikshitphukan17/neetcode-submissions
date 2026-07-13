class Solution {
    public String longestPalindrome(String s) {
        int[] res = {0,0};
        for(int i = 0;i<s.length();i++) {
            int[] pal1 = getPalindrome(i,i,s);
            int[] pal2 = getPalindrome(i,i+1,s);
            int l1 = pal1[0], r1 = pal1[1], l2 = pal2[0], r2 = pal2[1];
            int rl = res[0],rr = res[1];
            if(r2-l2>r1-l1){
                if(r2-l2>rr-rl){
                    res =new int[] {l2,r2};
                }
            } else {
                if(r1-l1>rr-rl){
                    res =new int[] {l1,r1};
                }
            }
        }
        return s.substring(res[0],res[1]+1);
        
    }

    public int[] getPalindrome(int l,int r, String s){
        while(l>=0 && r<s.length() && s.charAt(l) == s.charAt(r)){
            l--;
            r++;
        }
        return new int[]{l+1,r-1};
    }
}
