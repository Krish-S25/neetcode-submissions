class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [ [] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for v, u in prerequisites:
            adj[u].append(v)
            indegree[v] += 1
        courses_done = 0
        Q = deque() 
        for i,deg in enumerate(indegree):
            if deg == 0:
                Q.append(i)
        
        while Q:
            curr = Q.popleft()
            courses_done += 1

            if courses_done == numCourses:
                return True

            for nbr in adj[curr]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    Q.append(nbr)
            
        return False
            

            
                
            

        