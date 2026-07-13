class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.cnt = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.cnt,tweetId])
        self.cnt -=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.follows[userId].add(userId)
        for followee in self.follows[userId]:
            if followee not in self.tweets:
                continue
            l = len(self.tweets[followee])-1
            cnt,tweetId = self.tweets[followee][l]
            heapq.heappush(heap,[cnt,tweetId,l,followee])
        res = []
        n = 10
        while n>0 and heap:
            cnt,tweetId,l,followee = heapq.heappop(heap)
            res.append(tweetId)
            l-=1
            if l>=0:
                cnt,tweetId = self.tweets[followee][l]
                heapq.heappush(heap,[cnt,tweetId,l,followee])
            n-=1
        return res


        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)

        
