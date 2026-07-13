class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweet = defaultdict(list)
        self.cnt = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet[userId].append([self.cnt,tweetId])
        self.cnt -=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        res = []
        self.follows[userId].add(userId)
        for followeeId in self.follows[userId]:
            if followeeId not in self.tweet:
                continue
            n = len(self.tweet[followeeId])-1
            cnt,tweetId = self.tweet[followeeId][n]
            heapq.heappush(heap,[cnt,tweetId,n-1,followeeId])
        while heap and len(res)< 10:
            cnt,tweetId,n,followeeId = heapq.heappop(heap)
            res.append(tweetId)
            if n>=0:
                cnt,tweetId = self.tweet[followeeId][n]
                heapq.heappush(heap,[cnt,tweetId,n-1,followeeId])
        return res
            
        

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
        
