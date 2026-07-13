class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int totalGas = 0;
        int totalCost = 0;
        for(int i = 0;i<gas.length;i++){
            totalGas += gas[i];
            totalCost += cost[i];
            gas[i] -= cost[i];
        }
        if(totalCost>totalGas){
            return -1;
        }
        int res = -1;
        int remainingGas = 0;
        for(int i=0;i<gas.length;i++){
            int g = gas[i];
            remainingGas +=g;
            if(remainingGas>=0 && res==-1){
                res = i;
            }
            else if(remainingGas<0){
                res = -1;
                remainingGas = 0;
            }
        }
        return res;

        // -2  -2  -2  3   3

    
        
    }
}
