class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int l,r;
        l = 0;
        r = numbers.length-1;
        int s;
        var res = new int[2];
        while(l<r){
            s = numbers[l]+numbers[r];
            if(s<target){
                l++;
            }else if(s>target){
                r--;
            }else{
                res[0] = ++l;
                res[1] = ++r;
                return res;
            }
            
        }
        return  res;
        
    }
}
