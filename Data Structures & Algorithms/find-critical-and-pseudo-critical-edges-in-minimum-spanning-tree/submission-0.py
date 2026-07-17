class union_find():
        def __init__(self, n:int):
            self.parent = [i for i in range(n)]
            self.components = n

        def find(self, node: int):
            if self.parent[node] != node:
                self.parent[node] = self.find(self.parent[node]) 
            return self.parent[node]

        def union(self, node1: int, node2:int):
            root1 = self.find(node1)
            root2 = self.find(node2)
            if root1!=root2:
                self.parent[root2] = root1
                self.components-=1
                return True
            return False

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for ix, edge in enumerate(edges):
            edge.append(ix)
        edges.sort(key = lambda x: x[2]) #Based on edge weight

        def getMST( forbidden_idx = -1, include_idx = -1): 
            UF = union_find(n) #Basically make a system to get MST with forced inclusions and exclusions
            total_weight = 0

            if include_idx != -1:
                for u, v, weight, orig_idx in edges:
                    if orig_idx == include_idx:  #Must have the included edge
                        UF.union(u, v)
                        total_weight += weight
                        break

            for u,v,weight, new_idx in edges:
                if new_idx == forbidden_idx:  #Skip the forbidden edge
                    continue
                
                elif UF.union(u,v):  # When NOT part of same component
                    total_weight += weight
                
            if UF.components == 1:
                return total_weight
            else:
                return float('inf')
        
        base_MST = getMST() #No blocked or forbidden

        critical = []
        pseudo = []

        for u, v, w, orig_idx in edges:
            # Check if critical: omit edge entirely
            if getMST(forbidden_idx = orig_idx) > base_MST:
                critical.append(orig_idx)
            # Check if pseudo-critical: force edge first
            elif getMST(include_idx = orig_idx) == base_MST:
                pseudo.append(orig_idx)
                
        return [critical, pseudo]

        
        