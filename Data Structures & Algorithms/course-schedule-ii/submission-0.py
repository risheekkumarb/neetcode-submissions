from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for course,pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        q = deque([i for i,o in enumerate(indegree) if o==0])

        ans = []
        while q:
            course = q.popleft()
            ans.append(course)
            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return ans if len(ans) == numCourses else []