class TimeMap {
    Map<String,List<String[]>> map ;
    public TimeMap() {
        map =  new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        map.putIfAbsent(key,new ArrayList<>());
        map.get(key).add(new String[] {value,String.valueOf(timestamp)});
    }
    
    public String get(String key, int timestamp) {
        if(!map.containsKey(key))
            return "";
        var list = map.get(key);
        int l = 0,r=list.size()-1;
        String res="";
        while(l<=r){
            int m = (l+r)/2;
            var value = list.get(m)[0];
            var time = Integer.parseInt(list.get(m)[1]);
            if(time==timestamp)
                return value;
            else if(time>timestamp){
                r=m-1;
            } else{
                res = value;
                l=m+1;
            }
        }
        return res;
    }
}
