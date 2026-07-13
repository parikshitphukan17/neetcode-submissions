class Solution {
    List<List<String>> res;
    List<String> pal;
    

    public List<List<String>> partition(String s) {
        res = new ArrayList<>();
        pal = new ArrayList<>();
        dfs(0,s);
        return res;
        
    }

    public void dfs(int i,String s){
        if(i==s.length()){
            res.add(new ArrayList<>(pal));
            return;
        }
        for(int j =i;j<s.length();j++){
            if(isPalin(s,i,j)){
                pal.add(s.substring(i,j+1));
                dfs(j+1,s);
                pal.remove(pal.size()-1);
            }
        }
    }

    public boolean isPalin(String s,int l,int r){
        while(l<r){
            if(s.charAt(l)!=s.charAt(r))
                return false;
            l++;
            r--;
        }
        return true;
    }
}
