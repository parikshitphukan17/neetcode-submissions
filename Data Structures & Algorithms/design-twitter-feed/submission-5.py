class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.counter = 0
        self.tweets = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.counter -=1
        self.tweets[userId].append([self.counter,tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        followList = self.followMap[userId]
        followList.add(userId)
        heap = []
        for followee in followList:
            if followee in self.tweets:
                index = len(self.tweets[followee])
                cnt,tweetId = self.tweets[followee][index-1]
                heapq.heappush(heap,[cnt,tweetId,followee,index-1])
        res = []
        while heap and len(res) <10:
            cnt,tweetId,followee,index = heapq.heappop(heap)
            res.append(tweetId)
            if index-1>=0:
                cnt,tweetId = self.tweets[followee][index-1]
                heapq.heappush(heap,[cnt,tweetId,followee,index-1])
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
