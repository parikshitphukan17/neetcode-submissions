class Solution {
    Map<Character,Set<Character>> adj = new HashMap<>();
    Map<Character,Boolean> vis = new HashMap<>();
    List<Character> res = new ArrayList<>();
    public String foreignDictionary(String[] words) {
        for(int i=0;i<words.length;i++){
            String word1 = words[i];
            if(i+1==words.length){
                continue;
            }
            String word2 = words[i+1];
            int len1 = word1.length(), len2 = word2.length();
            int minLen = Math.min(len1,len2);
            if(len1>len2 && word1.substring(0,minLen).equals(word2.substring(0,minLen))){
                return "";
            }
            for(int j =0;j<minLen;j++){
                if(word1.charAt(j) == word2.charAt(j)){
                    continue;
                }
                adj.putIfAbsent(word1.charAt(j),new HashSet<>());
                adj.get(word1.charAt(j)).add(word2.charAt(j));
                break;
            }
        }

        for(String word:words){
            for(Character c:word.toCharArray()){
                if(!dfs(c)){
                    return "";
                }

            }
        }
        Collections.reverse(res);
        return res.stream()
                    .map(String::valueOf)
                    .collect(Collectors.joining());

      
    }

    // n->f
    // h->e
    // r->n
    // e->r
    // h->e->r->n->f

    public boolean dfs(Character src){
        if(vis.containsKey(src)){
            return vis.get(src);
        }
        vis.put(src,false);
        if(adj.containsKey(src)){
            for(Character nei:adj.get(src)){
                if(!dfs(nei)){
                    return false;
                }
            }
        }
        vis.put(src,true);
        res.add(src);
        return true;
    }

    // t->f
    // w->e
    // r->t
    // e->r
    // r->t

    // w   e   r   t   f
}
