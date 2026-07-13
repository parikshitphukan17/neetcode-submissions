class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> comb = new ArrayList<>();

        dfs(0,0,target,candidates,comb,res);
        return res;
        
    }

    public void dfs(int i, int s, int target, int[] candidates, 
    List<Integer> comb,List<List<Integer>> res) {
        if(s==target){
            res.add(new ArrayList<>(comb));
            return;
        }
        if(i==candidates.length || s>target){
            return;
        }
        comb.add(candidates[i]);
        dfs(i+1,s+candidates[i],target,candidates,comb,res);
        comb.remove(comb.size()-1);
        while(i+1<candidates.length && candidates[i] == candidates[i+1]){
            i++;
        }
        dfs(i+1,s,target,candidates,comb,res);
    }
}
