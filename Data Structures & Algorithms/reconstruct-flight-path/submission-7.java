class Solution {
    Map<String,List<String>> adj = new HashMap<>();
    List<String> res = new ArrayList<>();
    public List<String> findItinerary(List<List<String>> tickets) {
        tickets.sort((a,b) -> a.get(1).compareTo(b.get(1)));
        for(List<String>ticket:tickets){
            String src = ticket.get(0),dest = ticket.get(1);
            adj.putIfAbsent(src,new ArrayList<>());
            adj.get(src).add(dest);
        }
        dfs("JFK");
        Collections.reverse(res);
        return res;
    }

    public void dfs(String src){
        if(!adj.containsKey(src)){
            res.add(src);
            return;
        }
        while(!adj.get(src).isEmpty()){
            String dest = adj.get(src).remove(0);
            dfs(dest);
        }
        res.add(src);
    }




        // JFK <-> SEA
        // -> Hou

        // JFk <->
        
        
        // JFK - [Hou,Sea]
        // SEA - [JFK]
        // Hou - []

        // JFK - [Hou,SEA] [SEA]
        // Hou - []
        // JFK - [SEA] []
        // SEA - [JFK] []
        // JFK - []




        // HOU,JFK,SEA,JFK - reverse

        // start with JFK go through each nei in adj for the node and remove from adj 
        //while consuming each nei recursively and backtrack and then add
        // to res


        
        




}
