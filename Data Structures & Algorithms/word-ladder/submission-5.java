class Solution {
    Map<String,List<String>> map = new HashMap<>();
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        if(!wordList.contains(endWord) || beginWord.equals(endWord)){
            return 0;
        }
        wordList.add(beginWord);
        for(String word:wordList){
            map.putIfAbsent(word,new ArrayList<>());
            for(int j=0;j<word.length();j++){
                String nei = word.substring(0,j)+"*"+
                    word.substring(j+1,word.length());
                map.get(word).add(nei);
                map.putIfAbsent(nei,new ArrayList<>());
                map.get(nei).add(word);
            }
        }
        Deque<String> q = new LinkedList<>();
        Set<String> vis = new HashSet<>();
        q.addLast(beginWord);
        vis.add(beginWord);
        int res = 1;
        while(!q.isEmpty()){
            int size = q.size();
            while(size-->0){
                String word = q.removeFirst();
                if(word.equals(endWord)){
                    return res;
                }
                for(String nei:map.get(word)){
                    for(String neiWord:map.get(nei)){
                        if(!vis.contains(neiWord)){
                            System.out.println(neiWord);
                            q.addLast(neiWord);
                            vis.add(neiWord);
                        }
                    }
                }
            }
            res++;
        }
        return 0;
        
    }
}
