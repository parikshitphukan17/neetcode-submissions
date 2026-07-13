class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;
        Integer buy = null;
        for(int p:prices){
            if(buy == null){
                buy = p;
                continue;
            }
            if(p<buy){
                buy = p;
            } else {
                res = Math.max(res,p-buy);
            }

        }
        return res;

        
    }
}
