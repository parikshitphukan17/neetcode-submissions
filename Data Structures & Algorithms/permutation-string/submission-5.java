class Solution {
    public boolean checkInclusion(String s1, String s2) {
        int[] s1Cnt = new int[26];
        int[] s2Cnt = new int[26];
        if(s2.length()<s1.length()){
            return false;
        }
        for(int i=0;i<s1.length();i++){
            s1Cnt[s1.charAt(i)-'a']++;
            s2Cnt[s2.charAt(i)-'a']++;
        }
        int matches = 0;
        for(int i=0;i<26;i++){
            if(s1Cnt[i] == s2Cnt[i]){
                matches++;
            }
        }
        if(matches == 26){
            return true;
        }
        int l = 0;
        for(int r = s1.length();r<s2.length();r++){
            int rightChar = s2.charAt(r);
            int rightIndex = rightChar - 'a';
            s2Cnt[rightIndex]++;
            if(s2Cnt[rightIndex]==s1Cnt[rightIndex]){
                matches++;
            } else if (s2Cnt[rightIndex]-1==s1Cnt[rightIndex]){
                matches--;
            }
            int leftChar = s2.charAt(l);
            int leftIndex = leftChar - 'a';
            s2Cnt[leftIndex]--;
            if(s1Cnt[leftIndex]==s2Cnt[leftIndex]){
                matches++;
            } else if (s2Cnt[leftIndex]+1==s1Cnt[leftIndex]){
                matches--;
            }
            if(matches == 26)
                return true;
            l++;

        }
        return false;
    }
}
