class Twitter:

    def __init__(self):
        # (id, timestamp/order)
        self.tweets = defaultdict(list)
        # (id1=[id2])
        self.followers = defaultdict(set)
        self.count=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        self.tweets[userId].append([tweetId,self.count])
        print(self.tweets)
        

    def getNewsFeed(self, userId: int,limit=10) -> List[int]:
        allTweet = self.tweets[userId].copy()
        # [allTweet.extend(self.tweets[f].copy()) for f in self.followers[userId]]
        for followeeId in self.followers[userId]:
            allTweet.extend(self.tweets[followeeId])
            if len(allTweet)>limit:
                break
        allTweet.sort(key = lambda k: k[1], reverse=True)
        return [k[0] for k in allTweet][:10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)
        # print(self.followers)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # print(self.followers)
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
            # print(self.followers)
        
