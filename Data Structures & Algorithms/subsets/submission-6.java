class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> subSet = new ArrayList<>();
        dfs(nums,0,res,subSet);
        return res;
        
    }

    public void dfs(int[] nums, int i, List<List<Integer>> res, List<Integer> subSet){
        if(i == nums.length){
            res.add(new ArrayList<>(subSet));
            return;
        }
        subSet.add(nums[i]);
        dfs(nums,i+1,res,subSet);
        subSet.remove(subSet.size()-1);
        dfs(nums,i+1,res,subSet);
    }
}
