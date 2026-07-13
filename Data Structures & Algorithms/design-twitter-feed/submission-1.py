class Twitter:

    def __init__(self):
        self.cnt = 0
        self.followMap = defaultdict(set)
        self.tweets = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.cnt,tweetId])
        self.cnt -=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.followMap[userId].add(userId)
        minHeap = []
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId])-1
                cnt,tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap,[cnt,tweetId,index-1,followeeId])
        res = []
        while minHeap and len(res)<10:
            cnt,tweetId,index,followeeId = heapq.heappop(minHeap)
            res.append(tweetId)
            if index>=0:
                cnt,tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap,[cnt,tweetId,index-1,followeeId])
        return res


                


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

        
