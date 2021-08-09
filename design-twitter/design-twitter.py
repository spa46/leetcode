from collections import defaultdict

class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._follow = defaultdict(list)
        self._tweet = defaultdict(list)
        self._twttime = defaultdict(int)
        self.twtcnt = 0
        
    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        
        self._tweet[userId].append(tweetId)
        self._twttime[tweetId] = self.twtcnt
        self.twtcnt += 1
        
       
    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        
        n = self._tweet[userId][:]
        m = [ self._twttime[v] for v in self._tweet[userId] ]

        for f in self._follow[userId]:
            for u in self._tweet[f]:
                n.append(u)
                m.append(self._twttime[u])
        
        arr = sorted(zip(n,m), key=lambda v: v[1], reverse=True)
        return [v[0] for v in arr[:10]]
            

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId not in self._follow[followerId]:
            self._follow[followerId].append(followeeId)
            
    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self._follow[followerId]:
            self._follow[followerId].remove(followeeId)
            if not self._follow[followerId]:
                del self._follow[followerId]

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)