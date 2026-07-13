class Solution {

    public int[] dailyTemperatures(int[] temperatures) {

        Deque<int[]> stack = new LinkedList<>();
        Map<Integer,Integer> map = new HashMap<>();
        for(int t=temperatures.length-1;t>=0;t--){
            int temp = temperatures[t];
            while(!stack.isEmpty() && stack.peekLast()[0]<=temp) {
                stack.removeLast();
            }
            if(stack.isEmpty()){
                map.put(t,0);
            } else {
                map.put(t,stack.peekLast()[1]-t);
            }
            stack.addLast(new int[]{temp,t});
        }
        int[] res= new int[temperatures.length];
        for(int key:map.keySet()){
            res[key] = map.get(key);
        }
        return res;




      
        // 28,6                0
        // 40,5                0
        // 35,4 ,40,5          1
        // 36,3 ,40,5          2
        // 30,2, 36,3 40,5     1
        // 38,1 40,5           4
        // 30,0 38,1 40,5      1


        
    }
}
