class Solution {
    int M,N;
    public boolean isOneEditDistance(String s, String t) {
       
        M = s.length();
        N = t.length();
        return check(0,0,s,t,0);
        
        
    }

    public boolean check(int i,int j, String s, String t, int steps){
        if(steps>1){
            return false;
        }
        if(i == M && j ==N){
            return steps == 1;
        }
        if(i<M && j<N){
            if(s.charAt(i) == t.charAt(j)){
                return check(i+1,j+1,s,t,steps);
            } else {
                steps +=1;
                return check(i,j+1,s,t,steps) || check(i+1,j,s,t,steps) || check(i+1,j+1,s,t,steps);
            }
        } else {
            steps +=1;
            if(i<M){
                return check(i+1,j,s,t,steps);
            }
            return check(i,j+1,s,t,steps);
        }
    }
}
