class Solution {
    public List<String> generateParenthesis(int n) {

        List<String> res = new ArrayList<>();
        List<String> brackets = new ArrayList<>();
        dfs(n,n,brackets,res);
        return res;
        
    }

    public void dfs(int o, int c, List<String> brackets, List<String> res){
        if(o==0 && c ==0){
            res.add(String.join("",brackets));
            return;
        }
        if(c<o){
            return;
        }
        if(o>0)
        {
            brackets.add("(");
            dfs(o-1,c,brackets,res);
            brackets.remove(brackets.size()-1);
        }
        if(c>0) {
        brackets.add(")");
        dfs(o,c-1,brackets,res);
        brackets.remove(brackets.size()-1);
        }
        
    }
}
