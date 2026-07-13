class Solution {
    public int evalRPN(String[] tokens) {
        Deque<Integer>stack = new LinkedList<>();
        for(String t: tokens){
            if(!t.equals("+") && !t.equals("-") && !t.equals("*") && !t.equals("/")){
                stack.addLast(Integer.parseInt(t));
            } else {
                int n2 = stack.removeLast(), n1 = stack.removeLast();
                if(t.equals("+")){
                    stack.addLast(n1+n2);
                } else if (t.equals("-")){
                    stack.addLast(n1-n2);

                } else if (t.equals("*")){
                    stack.addLast(n2*n1);

                } else {
                    stack.addLast(n1/n2);

                }
            }

        }
        return stack.removeLast();





        // 1   2   +   3   *   4   -


        // [1,2]
        // 2+1     
        // [3,3]



        
    }
}
