class MinStack {

    Deque<Integer> min = new LinkedList<>();
    Deque<Integer> stack = new LinkedList<>();


    public MinStack() {
        
    }
    
    public void push(int val) {
        stack.addLast(val);
        if(min.isEmpty()){
            min.addLast(val);
            return;
        }
        if(val<min.peekLast()){
            min.addLast(val);
        } else {
            min.addLast(min.peekLast());
        }
        
    }
    
    public void pop() {
        stack.removeLast();
        min.removeLast();
        
    }
    
    public int top() {
        return stack.peekLast();
    }
    
    public int getMin() {
        return min.peekLast();

        
    }

    // 2   2   2   1   1   1   0   0
    // 2   3   4   1   5   7   0   1


}

