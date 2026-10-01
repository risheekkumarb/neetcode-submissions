from heapq import heapify, heappop
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.users = defaultdict(dict) # user -> posts # [(time, tweetId)], follows # [userIds]
        self.time  = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time -= 1
        user = self.users[userId] # either empty dict or filled dict
        user.setdefault('posts', []).append((self.time, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.users[userId]
        # all_users = list(user['follows'] if 'follows' in user else set() | set([userId]) )
        all_users = user.get('follows', set()) | {userId}
        all_posts = [p for u in all_users for p in self.users[u].get('posts', [])]
        heapify(all_posts)
        i = 0
        res = []
        while all_posts and i<10:
            i += 1
            res.append(heappop(all_posts)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        user = self.users[followerId]
        user.setdefault('follows', set([followeeId])).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        user = self.users[followerId]
        user.get('follows',{}).discard(followeeId)
        
