class Solution {
    int res = 0;
    public int countSubstrings(String s) {
        for(int i = 0;i<s.length();i++){
            check(i,i,s);
            check(i,i+1,s);
        }
        return res;

        
    }
    public void check(int l,int r,String s){
        while(l>=0 && r<s.length() && s.charAt(l) == s.charAt(r)){
            res++;
            l--;
            r++;
        }
    }
}
