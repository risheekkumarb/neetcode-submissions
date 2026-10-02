from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for pre,course in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        q = deque([i for i,o in enumerate(indegree) if o == 0])
        finish = 0
        while q:
            pre = q.popleft()
            finish += 1
            for course in adj[pre]:
                indegree[course] -= 1
                if indegree[course] == 0: q.append(course)
        return finish == numCourses