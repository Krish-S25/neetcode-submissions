import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heapL = []  #python priority works in min heap only

        for pnt in points:
            dist = pnt[0]**2 + pnt[1]**2
            heapq.heappush(heapL, (-dist, pnt))  
                        #Python has only minheap so **smallest -ve = largest +ve**
            if len(heapL)>k :
                heapq.heappop(heapL)  
                        #Maintain at most k elements in heapL by removing smallest -ve
        return [pnt for val, pnt in heapL]