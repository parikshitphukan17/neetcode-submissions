class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> perm = new ArrayList<>();
        boolean[] vis = new boolean[nums.length];
        for(int i =0;i<nums.length;i++){
            vis[i] = false;
        }
        dfs(nums,vis,perm,res);
        return res;

        
    }

    public void dfs(int[] nums, boolean[] vis,List<Integer> perm,List<List<Integer>> res){
        if(perm.size()==nums.length){
            res.add(new ArrayList<>(perm));
            return;
        }
        for(int i = 0;i<nums.length;i++){
            if(vis[i]){
                continue;
            }
            vis[i] = true;
            perm.add(nums[i]);
            dfs(nums,vis,perm,res);
            perm.remove(perm.size()-1);
            vis[i] = false;
        }

    }
}
