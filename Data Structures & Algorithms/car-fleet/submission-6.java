class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int[][] array = new int[position.length][2];
        for(int i=0;i<position.length;i++){
            array[i][0] = position[i];
            array[i][1] = speed[i];
        }

        Arrays.sort(array, Comparator.comparingInt(a -> a[0]));
        Deque<Double> stack = new LinkedList<>();
        for(int[] arr: array){
            int p = arr[0], s = arr[1];
            double cur = ((double)target-p)/s;
            if(stack.isEmpty()){
                stack.addLast(cur);
            } else {
                while(!stack.isEmpty() && stack.peekLast()<=cur){
                    stack.removeLast();
                }
                stack.addLast(cur);
            }
        }
        return stack.size();



        // 10
        // {0  1   4   7}
        // {1  2   2   1}


        // [10 4   3   3]

        
    }
}
