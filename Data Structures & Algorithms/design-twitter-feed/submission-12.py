from heapq import heapify, heappop, heappush

class Twitter:
    def __init__(self):
        self.time = 0
        self.users = {} # user --> posts (List[(time posted, postId)]), follows (set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users: self.users[userId] = {}
        self.time += 1
        up = self.users[userId].get('posts', [])
        up.append((-self.time, tweetId))
        self.users[userId]['posts'] = up

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users: return None
        user = self.users[userId]
        all_posts = user.get('posts', []).copy()
        user_follows = user.get('follows', [])
        for o in user_follows: all_posts.extend(self.users[o].get('posts',[]))
        heapify(all_posts)
        res = []
        for _ in range(10):
            if all_posts: res.append(heappop(all_posts)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # checks
        if followerId == followeeId: return None
        if followeeId not in self.users: self.users[followeeId] = {}
        if followerId not in self.users: self.users[followerId] = {}
        # get previous
        follows = self.users[followerId].get('follows', set())
        # assign and add
        follows.add(followeeId)
        self.users[followerId]['follows'] = follows

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # check if exists and remove
        if followeeId in self.users[followerId].get('follows', set()):
            self.users[followerId]['follows'].remove(followeeId)
