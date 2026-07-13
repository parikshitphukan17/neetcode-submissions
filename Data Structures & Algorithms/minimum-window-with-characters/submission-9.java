class Solution {
    public String minWindow(String s, String t) {
        Map<Character,Integer> cntT= new HashMap<>();
        Map<Character,Integer> cntS= new HashMap<>();
        for(Character c:t.toCharArray()){
            cntT.put(c,cntT.getOrDefault(c,0)+1);
        }
        int need = cntT.size();
        int have = 0;
        int l = 0;
        int res = s.length()+1;
        int[] resArray = new int[26];
        for(int r = 0;r<s.length();r++){
            var charR = s.charAt(r);
            cntS.put(charR,cntS.getOrDefault(charR,0)+1);
            if(cntT.containsKey(charR) && cntT.get(charR)==cntS.get(charR)){
                have++;
            }
            while(have==need && l<s.length()){
                if(r-l+1<res){
                    res = r-l+1;
                    resArray[0]=l;
                    resArray[1]=r;

                }
                var charL = s.charAt(l);
                cntS.put(charL,cntS.get(charL)-1);
                if(cntT.containsKey(charL) && cntS.get(charL)<cntT.get(charL)){
                    have--;
                }
                l++;
            }

        }
        if(res == s.length()+1){
            return "";
        } else{
            return s.substring(resArray[0],resArray[1]+1);
        }




    // h   0       1           2   3
    // n   3       3           3   3
    //     l   r   r   r   r   r   r   
    //     O   U   Z   O   D   Y   X   A   Z   V

    //     X   Y   Z

    //     have = 0
    //     need = 3
    //     while have == need:
    //         calcl lenght and shorten window

    }
}
