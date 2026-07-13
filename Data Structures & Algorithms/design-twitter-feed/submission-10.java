class Twitter {
    int count;
    Map<Integer,List<int[]>> tweetMap;
    Map<Integer,Set<Integer>> followMap;
    public Twitter() {
        count = 0;
        tweetMap = new HashMap<>();
        followMap = new HashMap<>();
        
    }
    
    public void postTweet(int userId, int tweetId) {
        tweetMap.putIfAbsent(userId,new ArrayList<>());
        tweetMap.get(userId).add(new int[]{count--,tweetId});
        
    }
    
    public List<Integer> getNewsFeed(int userId) {
        List<Integer> res = new ArrayList<>();
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(
            Comparator.comparingInt(a->a[0])
        );
        followMap.putIfAbsent(userId,new HashSet<>());
        followMap.get(userId).add(userId);
        for(int followeeId: followMap.get(userId)){
            if(!tweetMap.containsKey(followeeId)){
                continue;
            }
            var tweets = tweetMap.get(followeeId);
            int index = tweets.size()-1;
            int[] tweet = tweets.get(index);
            minHeap.offer(new int[] {tweet[0],tweet[1],followeeId,index});
        }
        while(res.size()<10 && minHeap.size()>0){
            var cur = minHeap.poll();
            res.add(cur[1]);
            if(cur[3]-1>=0){
                var tweets = tweetMap.get(cur[2]);
                int index = cur[3]-1;
                var tweet = tweets.get(index);
                int followeeId = cur[2];
                minHeap.offer(new int[] {tweet[0],tweet[1],followeeId,index});
            }
        }
        return res;

        
    }
    
    public void follow(int followerId, int followeeId) {
        followMap.putIfAbsent(followerId,new HashSet<>());
        followMap.get(followerId).add(followeeId);

        
    }
    
    public void unfollow(int followerId, int followeeId) {
        followMap.computeIfPresent(followerId, (k,v)
        -> {
                v.remove(followeeId);
                return v;
        });
        
    }
}
