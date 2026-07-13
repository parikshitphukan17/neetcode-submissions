class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> sub = new ArrayList<>();
        Arrays.sort(nums);
        dfs(0,nums,sub,res);
        return res;
    }

    public void dfs(int i, int[] nums, List<Integer> sub, List<List<Integer>> res){
        if(i == nums.length){
            res.add(new ArrayList<>(sub));
            return;
        }
        sub.add(nums[i]);
        dfs(i+1,nums,sub,res);
        sub.remove(sub.size()-1);
        while(i+1<nums.length && nums[i] == nums[i+1]){
            i++;
        }
        dfs(i+1,nums,sub,res);
    }
}
