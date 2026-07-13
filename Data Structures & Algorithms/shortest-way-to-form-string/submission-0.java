class Solution {
    int M,N;
    public int shortestWay(String source, String target) {
        M = source.length();
        N = target.length();
        return getSub(0,0,source,target,0);

        
    }

    public int getSub(int i,int j, String s,String t,int sub){
        if(j==N){
            return sub;
        }
        int curJ = j;
        while(i<M && s.charAt(i) != t.charAt(j)){
            i++;
        }
        while(i<M && j<N){
            if(s.charAt(i) == t.charAt(j)){
                j++;
            }
            i++;
        }
        if(j == curJ){
            return -1;
        }
        return getSub(0,j,s,t,sub+1);
    }

    // a   b   c
    // a   b   c   a   b   c

    // i
    // a   b   c
    // j
    // a   c   b   c   a


    // a   c
    // b   c
    // a

    // while i<M and j<N{
    //     find starting point
    //     while(i<M and s[i]!=t[j]){
    //         i++;
    //     }
    //     move i till i<M and increase j for each match
    //     while(i<M and j<N){
    //         if(s[i] == t[j]){
    //             j++;
    //         }
    //         i++;
    //         if(j ==curJ){
    //             return -1
    //         }
    //         check if j reached end? then return res else 
    //         (0,j)
    //     }
    // }





}
