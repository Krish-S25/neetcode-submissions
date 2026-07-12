class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        start = "JFK"
        adj = defaultdict(list)
        for u,v in tickets:
            heapq.heappush(adj[u], v)

        itn = []
        visited = set()

        def dfs(src):
            visited.add(src)

            while adj[src]:
                nbr = heapq.heappop(adj[src])
                dfs(nbr)
            
            itn.append(src)
        dfs(start)

        return itn[::-1]
