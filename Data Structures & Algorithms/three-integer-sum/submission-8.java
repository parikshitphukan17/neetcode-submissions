class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        int l,r;
        for(int i = 0;i<nums.length;i++){
            if(nums[i]>0){
                break;
            }
            if(i>0 && nums[i-1]==nums[i]){
                continue;
            }
            l = i+1;
            r = nums.length-1;
            while(l<r){
                int s = nums[i]+nums[l]+nums[r];
                if(s<0){
                    l++;
                } else if (s>0){
                    r--;
                } else{
                    res.add(Arrays.asList(nums[i],nums[l],nums[r]));
                    l++;
                    r--;
                    while (l<r && nums[l] == nums[l-1]){
                        l+=1;
                    }
                }

            }

        }
        return res;

        
    }
}
