from collections import defaultdict
from typing import List

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        # 1. DSU Data Structures (Using index integers 0 to n-1 instead of coordinates)
        parent = [i for i in range(n)]
        rank = [1] * n
        
        def find(i):
            if parent[i] != i:
                # Path compression optimization
                parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            root1 = find(i)
            root2 = find(j)
            
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root2] > rank[root1]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1
                return True        #When NODE1 and NODE2 in different Disjoint sets

            else :
                return False       #When NODE1 and NODE2 in SAME Disjoint sets

        # NESTED LIST instead of normal adj dictionary
        edges = []
        for i in range(n):
            x, y = points[i]
            for j in range(i+1, n):
                u, v = points[j]
                manhattan = abs(x - u) + abs(y - v)
                edges.append((manhattan, i, j)) #Tuple storage

        edges.sort()

        mst_cost = 0
        num_edges = 0
        for dist, u, v in edges:
            if union(u, v):  #in kruskal we find nodes outside current disjoint set
                mst_cost += dist
                num_edges +=1
                if num_edges == n-1:
                    break
                    
        return mst_cost