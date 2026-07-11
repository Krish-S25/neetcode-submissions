from collections import defaultdict
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        start = k 
        
        adj = defaultdict(list)
        for u, v, edge_cost in times:
            adj[u].append((v, edge_cost))
             #Built in edge cost { u : (v, cost(u,v))}
        delays = [float('inf')] * (n + 1)
        delays[start] = 0
        min_heap = [[0, start]]
        
        while min_heap:
            curr_delay, curr = heapq.heappop(min_heap)
            
            if curr_delay > delays[curr]: #ignores crass values
                continue
                
            for nbr, edge_cost in adj[curr]:
                if delays[nbr] > curr_delay + edge_cost:
                    delays[nbr] = curr_delay + edge_cost
                    heapq.heappush(min_heap, [delays[nbr], nbr])
        
        max_delay = max(delays[1:])
        if max_delay != float('inf'): 
            return max_delay 

        return -1