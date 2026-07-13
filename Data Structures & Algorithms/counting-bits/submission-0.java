class Solution {
    public int[] countBits(int n) {

        int[] dp = new int[n+1];
        int offset = 2;
        for(int i =1;i<=n;i++){
            if(offset*2 == i)
                offset = i;
            dp[i] += 1 + (i-offset>=0?dp[i-offset]:0);
        }
        return dp;

        // 1111
        // 0111

        //     0
        //    01
        //    10
        //    11
        //   100
        //   101
        //   110
        //   111
        //  1000= 0+1
        //  1001=01+1
        //  1010=10+1
        //  1011=11+1
        //  1100=100+1
        //  1101=101+1
        //  1110=110+1
        //  1111=111+1
        // 10000=
        
    }
}
