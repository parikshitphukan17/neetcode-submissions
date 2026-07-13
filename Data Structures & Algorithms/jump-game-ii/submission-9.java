class Solution {
    public int jump(int[] nums) {
        int l= 0,r= 0;
        int res = 0;
        while(r<nums.length-1){
            res++;
            int nextR=r;
            for(int i=l;i<=r;i++){
                nextR = Math.max(nextR,nums[i]+i);
            }
            l= r+1;
            r = nextR;
        }
        return res;

        
    }
}
