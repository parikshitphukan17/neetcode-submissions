class Solution {
    public int maxProduct(int[] nums) {

        int res = -11;
        int p=1,n=1;
        for(int num: nums){
            int maxVal = Math.max(num*p,num*n);
            res = Math.max(res,maxVal);
            int nexN = Math.min(num*p,num*n);
            n = Math.min(nexN,1);
            p = Math.max(maxVal,1);

        }
        return res;

//     -11 1   2   2
//   p 1   1   2   1       
//         1   2   -3  4   -2
//   m 1   1   1   -6

        
    }
}
