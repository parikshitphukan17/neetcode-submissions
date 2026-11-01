class Twitter:

    def __init__(self):
        self.followSet = defaultdict(set)
        self.tweets = defaultdict(list)
        self.cnt = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.cnt,tweetId])
        self.cnt -=1
    
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followSet[userId].add(userId)
        maxHeap = []
        for followeeId in self.followSet[userId]:
            tweets = self.tweets[followeeId]
            if not self.tweets[followeeId]:
                continue
            tweet = self.tweets[followeeId][-1]
            heapq.heappush(maxHeap,tweet + [followeeId,len(tweets)-1])
        res = []
        while maxHeap and  len(res)<10:
            cnt,tweetId,followeeId,index = heapq.heappop(maxHeap)
            res.append(tweetId)
            index -=1
            if index>=0:
                heapq.heappush(maxHeap,self.tweets[followeeId][index]+[followeeId,index])
        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followSet[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in  self.followSet[followerId]:
             self.followSet[followerId].remove(followeeId)
    
