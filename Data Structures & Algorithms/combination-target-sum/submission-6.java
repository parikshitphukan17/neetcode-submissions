class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> comb = new ArrayList<>();
        dfs(0,0,target,nums,res,comb);
        return res;

        
    }

    public void dfs(int i, int s, int target, int[] nums, 
        List<List<Integer>> res, List<Integer> comb) {
        if(i == nums.length || s>target){
            return;
        }
        if(s == target){
            res.add(new ArrayList<>(comb));
            return;
        }
        comb.add(nums[i]);
        dfs(i,s+nums[i],target, nums, res, comb);
        comb.remove(comb.size()-1);
        dfs(i+1, s, target, nums, res, comb);
    }
}
